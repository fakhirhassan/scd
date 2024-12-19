from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request , 'base.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request , user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render(request , "login.html")

def signup(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        
        if User.objects.filter(email=email).exists():
            return HttpResponse("An account with this email already exists!!")
        
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
     return render(request , 'signup.html')

def ManagerSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        organization = request.POST.get('organization')
        cnic = request.POST.get('cnic')
        confirm_cnic = request.POST.get('confirm_cnic')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Your password and confirm password do not match!!")

        # Check if CNIC and confirm CNIC match
        if cnic != confirm_cnic:
            return HttpResponse("Your CNIC and confirm CNIC do not match!!")

        # Check if the user with the provided email already exists
        if User.objects.filter(email=email).exists():
            return HttpResponse("An account with this email already exists!!")

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        # Additional fields for manager
        user.profile.organization = organization
        user.profile.cnic = cnic
        user.profile.save()

        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'ManagerSignup.html')

def tournament(request):
    if request.method == "POST":
        team_name = request.POST['team_name']
        player_1_id = request.POST['player_1_id']
        player_1_name = request.POST['player_1_name']
        player_2_id = request.POST['player_2_id']
        player_2_name = request.POST['player_2_name']
        player_3_id = request.POST['player_3_id']
        player_3_name = request.POST['player_3_name']
        player_4_id = request.POST['player_4_id']
        player_4_name = request.POST['player_4_name']
        substitute_id = request.POST['substitute_id']
        substitute_name = request.POST['substitute_name']
        tournament = request.POST['tournament']

        Team.objects.create(
            team_name=team_name,
            player_1_id=player_1_id, player_1_name=player_1_name,
            player_2_id=player_2_id, player_2_name=player_2_name,
            player_3_id=player_3_id, player_3_name=player_3_name,
            player_4_id=player_4_id, player_4_name=player_4_name,
            substitute_id=substitute_id, substitute_name=substitute_name,
            tournament=tournament
        )
        return redirect('Viewteams')
    return render(request , 'tournament.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'hassanshaba0987@gmail.com',  # Sender's email address
            ['fakhirhassanllc@gmail.com'],  # List of recipient(s)
            fail_silently=False,
        )
        return HttpResponseRedirect('/contact/?success=true')

    return render(request, 'contact.html')



def Viewteams(request):
    teams = Team.objects.all()
    return render(request, 'Viewteams.html', {'teams': teams})

def game(request):
    game = Game.objects.all()
    return render(request, 'game.html', {'game': game})