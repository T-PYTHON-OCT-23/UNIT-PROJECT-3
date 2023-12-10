from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from django.db.utils import IntegrityError
from .models import Profile




def register_view(request : HttpRequest):
    # request.user.is_authenticated

    msg=None
    try:
        if request.method=="POST":

            user = User.objects.create_user( username=request.POST["username"] , first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"] , password=request.POST['password'] )
            user.save()

            profile = Profile(user=user , gender = request.POST["gender"])
            if "avatar" in request.FILES: profile = request.FILES["avatar"]
            profile.save()

            return redirect('main:home_view')
        

    except IntegrityError as e:
        msg="this username was token , please select another username"
        
    except Exception as e:
       # print(e.__class__)
        msg= f"somthing wrong {e}"

    return render(request ,'account/register.html' , {"msg" : msg})




def login_view(request : HttpRequest):
    msg = None
    
    if request.method=="POST":
        user = authenticate(request ,username=request.POST["username"] ,password=request.POST['password'])

    # if i have this user
        if user:
            login(request,user)
            return redirect('main:home_view')
        else:
            msg= "Please fill username and password"

    return render( request , 'account/login.html' , { "msg" : msg })



def logout_view(request : HttpRequest):
    if request.user.is_authenticated:
        logout(request)   
    return redirect('main:home_view')



def profile_view(request: HttpRequest, user_id):
    try: 
        user = User.objects.get(id=user_id)
    except:
        return render(request, 'main/error_page.html')
    

    return render(request, 'account/profile.html', {"user":user})



def update_profile_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                try:
                    profile : Profile = request.user.profile
                except Exception as e:
                    profile = Profile(user=user, gender=request.POST["gender"])
                    profile.save()

                return redirect("account:profile_view", user_id = request.user.id)

            else:
                return redirect("account:login_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something wrong {e}"

    return render(request, "account/update.html", {"msg" : msg})