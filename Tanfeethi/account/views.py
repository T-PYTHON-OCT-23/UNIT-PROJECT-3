from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout 
from django.db.utils import IntegrityError
from .models import Profile
from main.models import Reservation
from django.shortcuts import render, get_object_or_404






def register_view(request : HttpRequest):
    # request.user.is_authenticated

    msg=None
    try:
        if request.method=="POST":

            user = User.objects.create_user( username=request.POST["username"] , first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"] , password=request.POST['password'] )
            user.save()

            profile = Profile(user=user , gender = request.POST["gender"] )
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



def profile_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_profile = Profile.objects.get(user=user)
        reservations = Reservation.objects.filter(passenger=user)
        flights = [reservation.flight for reservation in reservations]
    except Profile.DoesNotExist:
        return render(request, 'main/error_page.html', {'error_message': 'Profile not found'})
    except User.DoesNotExist:
        return render(request, 'main/error_page.html', {'error_message': 'User not found'})
    except Exception as e:
        return render(request, 'main/error_page.html', {'error_message': str(e)})

    return render(request, 'account/profile.html', {"user": user, 'user_profile': user_profile, 'flights': flights})
    




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
                    profile = Profile(user=user, birth_date=request.POST["birth_date"])
                    profile = Profile(user=user, gender=request.POST["gender"])
                    profile.save()

                profile.birth_date = request.POST["birth_date"]
                profile.gender = request.POST["gender"]

                return redirect("account:profile_view", user_id = request.user.id)

            else:
                return redirect("account:login_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something wrong {e}"

    return render(request, "account/update.html", {"msg" : msg})





