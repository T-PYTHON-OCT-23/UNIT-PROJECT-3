from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpRequest, HttpResponse
from . models import Property,Rental,Sale,Comment
from datetime import datetime , date
from accounts.models import UserProfile ,User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg, Sum, Max, Min
from favorite.models import Favorite

# Create your views here.
def add_property_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_property= Property(title=request.POST["title"],
                                    description=request.POST["description"],
                                    rental_price=request.POST["rental_price"],
                                    sale_price=request.POST["sale_price"],
                                    bedrooms=request.POST["bedrooms"],
                                    bathrooms=request.POST["bathrooms"],
                                    floor=request.POST["floor"],
                                    area=request.POST["area"],
                                    location=request.POST["location"],
                                    owner=request.user)
            if 'image' in request.FILES:
                new_property.image=request.FILES["image"]

            new_property.save()
            return redirect('property:property_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'property/add_property.html',{'msg':msg})
def update_property_view(request:HttpRequest,property_id):
    msg=None
    try:
        update_property=Property.objects.get(id=property_id)
        if not request.user == update_property.owner:
            return render(request, "main/not_authorized.html", status=401)
        else:
            if request.method == "POST":
                update_property.title=request.POST["title"]
                update_property.description=request.POST["description"]
                update_property.rental_price=request.POST["rental_price"]
                update_property.sale_price=request.POST["sale_price"]
                update_property.bedrooms=request.POST["bedrooms"]
                update_property.bathrooms=request.POST["bathrooms"]
                update_property.area=request.POST["area"]
                update_property.location=request.POST["location"]
                if 'image' in request.FILES:
                    update_property.image=request.FILES["image"]

                update_property.save()
                return redirect ('property:detail_property_view',property_id=update_property.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'property/update_property.html',{"update_property":update_property,'msg':msg})
def delete_property_view(request:HttpRequest,property_id):
    try:
        delete_property=Property.objects.get(id=property_id)
        if not request.user == delete_property.owner:
            return render(request, "main/not_authorized.html", status=401)
        else:
            delete_property.delete()
            return redirect('accounts:user_profile_view', user_id =request.user.id)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/detail_property.html',{"msg":msg})
def property_home_view(request:HttpRequest):
    try:
        #view_property=Property.objects.all()
        view_property=Property.objects.exclude(rental__rent_to__gte= date.today())
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'property/property_home.html',{'view_property':view_property})
def detail_property_view(request:HttpRequest,property_id):
    try:
        property_detail=Property.objects.get(id=property_id)
        
        comments = Comment.objects.filter(property=property_detail)

        is_favored = request.user.is_authenticated and Favorite.objects.filter(property=property_detail, user=request.user).exists()

        comment_max = Comment.objects.filter(property=property_detail).aggregate(Max("rating"))["rating__max"]
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'property/detail_property.html',{"property_detail":property_detail,'comments':comments,'comment_max':comment_max,"is_favored":is_favored})
def rental_property_view(request:HttpRequest,property_id):
    msg=None
    try:
        rental=Property.objects.get(id=property_id)
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            if request.method == "POST":
                rent_from=datetime.strptime(request.POST['rent_from'], '%Y-%m-%d').date()
                rent_to=datetime.strptime(request.POST['rent_to'], '%Y-%m-%d').date()
                rental_date=Rental(property=rental,tenant=request.user,rent_from=rent_from,rent_to=rent_to)
                is_rented_to_current_user = Rental.objects.filter(tenant=request.user,
                                                                property=rental,
                    rent_from__lte=rent_to,
                    rent_to__gte=rent_from).exists()
                overlapping_rentals = Rental.objects.filter(
                    property=rental,
                    rent_from__lte=rent_to,
                    rent_to__gte=rent_from
                )
                if (rent_to - rent_from).days < 30:
                    return render(request, 'property/rent.html', {'rental':rental,'error_message': 'Minimum rental duration is one month.'})
                elif not is_rented_to_current_user :
                    rental_date.save()
                    return redirect('accounts:user_profile_view',user_id =request.user.id)
                elif overlapping_rentals.exists():
                    return render(request, 'property/rent.html', {'rental': rental, 'error_message': 'This property is already rented for the specified dates.'})
                else:
                    rental_date.save()
                    return redirect('accounts:user_profile_view',user_id =request.user.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'property/rent.html',{'rental':rental,"msg":msg})
def sale_property_view(request:HttpRequest,property_id):
    msg=None
    try:
        sale=Property.objects.get(id=property_id)
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            sale_done=Sale(buyer=request.user, seller=sale.owner, property=sale)
            sale_done.save()
            sale.owner=request.user
            sale.save()
            return redirect("accounts:user_profile_view",user_id=request.user.id)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/detail_property.html',{"msg":msg})
def rental_property_list_view(request:HttpRequest):
    try:
        view_property = Property.objects.filter(rental_price__gt=0)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'property/rental_list.html',{'view_property':view_property})
def sale_property_list_view(request:HttpRequest):
    try:
        view_property = Property.objects.filter(sale_price__gt=0)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'property/sale_list.html',{'view_property':view_property})

def sold_properties_view(request):
    msg=None
    try:
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            sales = Sale.objects.filter(seller=request.user)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/sold_properties.html',{'sales': sales,'msg':msg})
def purchases_properties_view(request):
    msg=None
    try:
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:

            purchases= Sale.objects.filter(buyer=request.user)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/purchases_properties.html',{'purchases': purchases,'msg':msg})
def rented_properties_view(request):
    msg=None
    try:
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            rented= Rental.objects.filter(property__owner=request.user)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/rented_properties.html',{'rented': rented,'msg':msg})
def rented_by_you_view(request):
    msg=None
    try:
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            rented= Rental.objects.filter(tenant=request.user)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/rented_by_you.html',{'rented': rented,'msg':msg})

def property_customers_view(request:HttpRequest):
    msg=None
    
    try:
        if not request.user.is_authenticated or request.user.has_perm('property.view_property'):
            return render(request, "main/not_authorized.html", status=401)
        
        else:
            property_instance = Property.objects.all()
            

                # Get tenants from rental records
            
            for i in property_instance:
                    rental_tenants = Rental.objects.filter(property__owner=request.user).values_list('tenant', flat=True)

                        # Get buyers from sale records
                    sale_buyers = Sale.objects.filter(seller=request.user).values_list('buyer', flat=True)

                        # Combine the lists of tenants and buyers to get unique customers
                    customer_ids = set(list(rental_tenants) + list(sale_buyers))

                        # Query the User model to get customer details
                    
                    customers = User.objects.filter(id__in=customer_ids)
                    
    except Exception as e:
         
         msg = f"An error occured, please fill in all fields and try again . {e}"
    try:     
        return render(request, 'property/customers.html', {'customers': customers,'msg':msg})
    except:
        msg=f"You don't have any customers yet"
        return render(request, "main/not_Found.html",{"msg":msg})
def search_results_view(request: HttpRequest):
    msg=None
    try:
        if "search" in request.GET:
            keyword = request.GET["search"]
            view_property = Property.objects.filter(title__contains=keyword)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"


    return render(request, "property/search.html", {"view_property" : view_property,'msg':msg})
def add_comment_view(request: HttpRequest, property_id):
    msg=None
    try:
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)
        else:
            if request.method == "POST":

                if not request.user.is_authenticated:
                    return render(request, "main/not_authorized.html", status=401)

                property = Property.objects.get(id=property_id)
                new_comment = Comment(property=property, user=request.user, text=request.POST["text"],rating=request.POST["rating"])  
                new_comment.save()
                return redirect("property:detail_property_view", property_id=property.id)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'property/detail_property.html',{"msg":msg})
def comment_view(request:HttpRequest):
    if not request.user.has_perm("property.view_comment"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        comments=Comment.objects.order_by('-created_at').all()
    return render(request,'property/comments_view.html',{'comments':comments})
def comment_detail_view(request:HttpRequest,comment_id):
    if not request.user.has_perm("property.view_comment"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        comments=Comment.objects.filter(id=comment_id).order_by('-created_at')
    return render(request,'property/comment.html',{'comments':comments})

def delete_comment_view(request:HttpRequest,comment_id):
    if not request.user.is_authenticated and request.user.has_perm("property.delete_comment"):
        return render(request, "main/not_authorized.html", status=401)
    else:
       
        comments=Comment.objects.get(id=comment_id)
        comments.delete()
        return redirect('property:comment_view')
    
def rent_view(request:HttpRequest):
    if not request.user.has_perm("property.view_rental"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        rent=Rental.objects.order_by('-rent_from').all()
    return render(request,'property/rent_view.html',{'rent':rent})
def rent_detail_view(request:HttpRequest,rent_id):
    if not request.user.has_perm("property.view_rental"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        rent=Rental.objects.filter(id=rent_id).order_by('-rent_from')
    return render(request,'property/rent_detail.html',{'rent':rent})

def delete_rent_view(request:HttpRequest,rent_id):
    if not request.user.is_authenticated and request.user.has_perm("property.delete_rental"):
        return render(request, "main/not_authorized.html", status=401)
    else:
       
        rent=Rental.objects.get(id=rent_id)
        rent.delete()
        return redirect('property:rent_view')
    
def sale_view(request:HttpRequest):
    if not request.user.has_perm("property.view_sale"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        sale=Sale.objects.order_by('-purchase_date').all()
    return render(request,'property/sale_view.html',{'sale':sale})
def sale_detail_view(request:HttpRequest,sale_id):
    if not request.user.has_perm("property.view_sale"):
        return render(request, "main/not_authorized.html", status=401)
    else:
        sale=Sale.objects.filter(id=sale_id).order_by('-purchase_date')
    return render(request,'property/sale_detail.html',{'sale':sale})

def delete_sale_view(request:HttpRequest,sale_id):
    if not request.user.is_authenticated and request.user.has_perm("property.delete_sale"):
        return render(request, "main/not_authorized.html", status=401)
    else:
       
        sale=Sale.objects.get(id=sale_id)
        sale.delete()
        return redirect('property:sale_view')