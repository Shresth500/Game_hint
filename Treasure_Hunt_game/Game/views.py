from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Treasure_Hunt_game.settings import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.db import models
from .models import Scoreboard,Puzzle,Answer,Clues
from django.template import loader
from django.views.decorators.csrf import csrf_protect


dead_ends = 2
number_of_answer = 1
Number_of_clues = 5

i=0

userid = None
name = None
score=0
# Create your views here.
def home(request):
    return render(request,"Game/index.html")


@csrf_protect
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
        myuser2 = Scoreboard.objects.create(user=myuser,first_name = fname,last_name = lname,email=email)
        myuser2.save()
        
        myuser.save()
        
        
        messages.success(request,"Your Account is created")
        
        
        return redirect("signin")
    return render(request,"Game/signup.html")

@csrf_protect
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
            return render(request,"Game/account.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")
    
    return render(request,"Game/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"You have successfully logged out of your account")
    return redirect('home')

def account(request):
    return render(request,"Game/account.html")

def start_game(request):
    userid = request.session.get('user_id')
    user = User.objects.get(id=userid)
    det = Scoreboard.objects.get(email = user.email)
    #user=User.objects.get(id=userid)
    questions  = Puzzle.objects.all()
    quest = []
    for quests in questions:
        quest.append({"questions":quests.question,
                      "images":quests.image.url,
                      'answer':quests.Getsolution(),
                      'clues':quests.GetClues()})
        

    payload = {'status':True,'quest':quest}

    image_url = 'River.png'
    context = {'image_url': image_url}
    #return JsonResponse(payload)
    return render(request,"Game/start_game.html",context)

def details(request):
    userid = request.session.get('user_id')
    user = User.objects.get(id=userid)
    det = Scoreboard.objects.get(email = user.email)
    #print(user.score)
    dict1 = {'fname': user.first_name, 
            'lname': user.last_name,
            'email': user.email,
            'score':det.score}
    print(dict1)
    return render(request, "Game/details.html", dict1)

def stats(request):
    overall_data = Scoreboard.objects.all().order_by('score').values()
    context = {
        'member':overall_data
    }
    template = loader.get_template("Game/stats.html")
    return HttpResponse(template.render(context,request))

def ends(request):
    return render(request,"Game/end.html")