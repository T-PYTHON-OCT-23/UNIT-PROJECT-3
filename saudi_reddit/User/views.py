
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate , logout 
from django.contrib.auth.models import User as userauth
from User.models import Profile 
from django.contrib.auth.decorators import login_required
from User.models import Post , Comment 
from subreddit.models import Subreddit
from django.http import JsonResponse
import random


def generate_username(request):
    # Replace this list with your actual list of suggestions
    adjectives = ["spark", "gun", "freedom", "zenith", "sapphire", "lunar", "whispering", "nebula", "rhythm", "quasar",
                  "stellar", "celestial", "cosmic", "moonlight", "sunbeam", "nightingale", "galactic", "astro", "void",
                  "ethereal", "amber", "skyward", "infinity", "lucent", "phantom", "echo", "silhouette", "velvet",
                  "quintessential", "whirlwind", "lucid", "moonshadow", "cosmic", "dreamweaver", "quantum", "serendipity",
                  "pulse", "stardust", "azure", "harmony", "astral", "luminescent", "quasar", "cascade", "solar", "lucent"]
    nouns = ["nomad", "phoenix", "rebel", "quest", "serenade", "nomad", "wanderer", "rebel", "quasar", "quest",
             "storyteller", "adventurer", "explorer", "enigma", "guru", "adventurer", "voyager", "explorer", "catalyst",
             "drifter", "quasar", "quietus", "arcane", "legend", "navigator", "chronicle", "expanse", "whisper", "wisdom",
             "willow", "elixir", "quasar", "quandary", "quiescence", "quadrant", "quartet", "quantum", "quietude", "solace",
             "sanctuary", "quiver", "quintessence", "chiaroscuro", "nurturer", "labyrinth", "wisdom", "specter", "sphinx",
             "sorcerer", "fable", "harlequin", "cynosure", "gazetteer", "zephyr", "walnut", "lagoon", "sonnet", "lexicon",
             "zest", "cerulean", "quadrant", "elixir", "melody", "spectacle", "lagoon", "quintessence", "chiaroscuro",
             "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus",
             "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse",
             "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody",
             "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary",
             "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar",
             "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon", "walnut", "zest", "cerulean", "quadrant", "lyricist",
             "elixir", "melody", "walnut", "spectacle", "lagoon", "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma",
             "sanctuary", "quandary", "lullaby", "cynosure", "labyrinth", "willow", "nimbus", "labyrinth", "sustenance",
             "quasar", "cascade", "labyrinth", "wisp", "nectar", "quiescence", "expanse", "silhouette", "sonnet", "lexicon",
             "walnut", "zest", "cerulean", "quadrant", "lyricist", "elixir", "melody", "walnut", "spectacle", "lagoon",
             "quintessence", "chiaroscuro", "nurturer", "whimsy", "enigma", "sanctuary", "quandary", "lullaby", "cynosure",
             "labyrinth", "willow", "nimbus", "labyrinth", "sustenance", "quasar", "cascade", "labyrinth", "wisp", "nectar",
             "quiescence", "expanse", "silhouette", "sonnet", "lexicon"]
    suggested_username = f"{random.choice(adjectives)}_{random.choice(nouns)}"
    if not check_backend_username(suggested_username):
        return JsonResponse({'suggested_username': suggested_username})
    else:
        return generate_username(request)


def signup(request):
    msg=""
    try:
        
        if request.method == 'POST':
                full_name = request.POST.get('full_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = userauth.objects.create_user(username=username,email=email,password=password)
                Profile.objects.create(user=user, email=email,full_name=full_name)
                user = authenticate(request, username=username, password=password)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/')
        else:
            return render(request, 'registration/signup.html', {'msg':msg})
    except Exception as e:
        msg=e
        return redirect('User:signup')

def user_login(request):
    msg=""
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                if not remember_me:
                    request.session.set_expiry(0)  # Session expires when the browser is closed
                return redirect('/')
            else:
                msg="Invalid username or password"
                return render(request, 'registration/login.html', {'msg':msg})
    else:   
        return render(request, 'registration/login.html', {'msg':msg})


def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def edit_profile(request):
    
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        if request.POST.get('password'): 
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
        if request.POST.get('username'):
            username = request.POST.get('username')
            user.username = username
            user.save()
        if request.POST.get('email'):
            email = request.POST.get('email')
            user.email = email
            profile.email = email
            profile.save()
            user.save()
        if request.POST.get('full_name'):
            full_name = request.POST.get('full_name')
            profile.full_name = full_name
            profile.save()
        if request.POST.get('bio'):
            bio = request.POST.get('bio')
            profile.bio = bio
            profile.save()
        if request.FILES.get('image'):
            image = request.FILES.get('image')
            profile.image = image
            profile.save()
        return redirect('User:profile_with_username', username=user.username)
    else:
        return render(request, 'registration/edit_profile.html', {'profile': profile})



def check_email(request):
    if request.method == 'GET':
        email = request.GET.get('email', '')
        # Perform a check to see if the email is already used in your database
        is_used = userauth.objects.filter(email=email).exists()
        return JsonResponse({'is_used': is_used})
    return JsonResponse({'is_used': False})  # Default response if not a GET request




def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        # Perform a check to see if the email is already used in your database
        is_used = userauth.objects.filter(username=username).exists()
        return JsonResponse({'is_used': is_used})
    return JsonResponse({'is_used': False})  # Default response if not a GET request




def check_backend_username(username):
    return userauth.objects.filter(username=username).exists()


def profile_Data(request,username):
    
    userauth1 = userauth.objects.get(username=username)
    user = Profile.objects.get(user=userauth1)
    
    posts = Post.objects.filter(author=userauth1)
    comments = Comment.objects.filter(author=userauth1)
    subreddits = Subreddit.objects.filter(subscribers=userauth1)
    author_subreddits = Subreddit.objects.filter(author=userauth1)
    
    user_profile = {
        
        'username': username,
        'email': user.email,
        'full_name': user.full_name,
        'bio': user.bio,
        'image': user.image.url if user.image else '',
        'created_at': user.created_at,
        'updated_at': user.updated_at,
        'post': posts,
        'comment': comments,
        'subreddit': subreddits,
        'author_subreddits': author_subreddits,
        'last_login': userauth1.last_login,
        
        
    }
    
    return render(request, 'registration/profile.html', {'user_profile': user_profile})


