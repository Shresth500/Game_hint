from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Treasure_Hunt_game.settings import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.db import models
from .models import Scoreboard


userid = None
name = None
score=0
# Create your views here.
def home(request):
    return render(request,"Game/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('Username')
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        password = request.POST['password']
        email=request.POST['email']
        confirm_passwrord = request.POST['confirmpassword']
        
        # if the user is already being created in the database then it will not be able to create it again
        if User.objects.filter(username=username):
            messages.error(request,"User name already exists please try another usename")
        
            # Checking for email
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already taken")
            return redirect("home")
        
        
        if password != confirm_passwrord:
            messages.error(request,"Password doesnot match")
        
        
        if not username.isalnum():
            messages.error(request,"username should consist of alphanumberic characters")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username=username,email=email,password=password)
        myuser.first_name=fname
        myuser.last_name=lname
        user1 = Scoreboard.objects.create(first_name = fname,last_name = lname,score=0)
        
        myuser.save()
        
        
        messages.success(request,"Your Account is created")
        
        
        return redirect("signin")
    return render(request,"Game/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            #user1 = User.objects.get(username)
            userid = user.id
            request.session['user_id'] = userid
            login(request,user)
            fname=user.first_name
            return render(request,"Game/account.html",{'fname':fname},{'new_url': '/new_url'})
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")
    
    return render(request,"Game/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"You have successfully logged out of your account")
    return redirect('home')

def account(request):
    userid = request.session.get('user_id')
    return render(request,"Game/account.html",{'fname':User.objects.get(userid).first_name})

def start_game(request):
    return render(request,"Game/start_game.html",{'new_url': '/account'})

def details(request):
    userid = request.session.get('user_id')
    user = User.objects.get(id=userid)
    #print(user.score)
    dict1 = {'fname': user.first_name, 
            'lname': user.last_name,
            'email': user.email,}
    print(dict1)
    return render(request, "Game/details.html", dict1)

def stats(request):
    return render(request,"Game/stats.html")