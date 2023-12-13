from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Art, Review
from favorites.models import Favorite

# Create your views here.
def add_art_view(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, "main/not_autherized.html" , status=401)
    
    msg = None
    if request.method == "POST":
        try:
            new_art = Art(poster=request.POST["poster"], title=request.POST["title"])
            if "poster" in request.FILES:
                new_art.poster = request.FILES["poster"]

            new_art.save()
            return redirect("Art:art_home_view")
        except Exception as e:
            msg = f"An error occured, please fill in all fields and try again . {e}"

    return render(request, "Art/add.html" , {"msg" : msg})



def art_home_view(request: HttpRequest):
    art = Art.objects.all()
    return render(request,"Art/art_home.html",{'arts':art})




def art_detail_view(request:HttpRequest, art_id):
    art_detail = Art.objects.get(id=art_id)
    reviews = Review.objects.filter(art=art_detail)

    #check if current logged in user has favored this art
    is_favored = request.user.is_authenticated and Favorite.objects.filter(art=art_detail, user=request.user).exists()

    return render(request, "Art/art_detail.html",{"art" : art_detail, "reviews" : reviews, "is_favored" :is_favored})


def update_art_view(request: HttpRequest, art_id):

    if not request.user.is_staff:
        return render(request, "main/not_authorized.html", status=401)
    
    art = Art.objects.get(id=art_id)

    if request.method == "POST":
        art.poster = request.POST["poster"]
        art.title = request.POST["title"]

        art.save()

        return redirect('Art:art_detail_view', art_id=art.id)
    
    return render(request, "Art/update.html", {"art" : art })

def delete_art_view(request: HttpRequest, art_id):
    #check for delete permission on art
    if not request.user.has_perm("Art.delete_art"):
        return render(request, "main/not_authorized.html", status=401)
    art =art.objects.get(id=art_id)
    art.delete()

    return redirect("Art:art_home_view")


def search_results_view(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        art = Art.objects.filter(title__contains=keyword)
    else: 
       art =Art.objects.all()

    return render(request, "Art/search.html", {"art" : art})

def add_review_view(request: HttpRequest , art_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        
        art_obj = Art.objects.get(id= art_id)
        new_review = Review(art=art_obj, user=request.user,  comment=request.POST["comment"])  
        new_review.save()
        return redirect("Art:art_detail_view", art_id=art_obj.id)
