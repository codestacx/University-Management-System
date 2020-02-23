from django.shortcuts import render,redirect
from django.http import HttpResponse
#import all models
from candidates.models.User import User
#flash messages
from django.contrib import messages
from django.db import connection
# Login Controller


def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        role = 'candidate'
        #User Authentications

        count = User.objects.filter(email=email,password=password,role=role).count()
        if(count>0):
            u = User.objects.filter(email=email,role=role).values('id','isComplete').get()
            request.session['user_logged'] = True
            request.session['user_id'] = u['id']
            request.session['isComplete'] = u['isComplete']
            return redirect('index')
        else:
            messages.error(request,'Invalid email or password')
            return render(request,'pages/login/login.html')

    else:
        return render(request,'pages/login/login.html')



#sign up

def signup(request):
    if request.method=='POST':
        email = request.POST['mail']
        password = request.POST['password']
        status = User.objects.create(email=email,password=password,role='candidate')
        if(status):
            messages.success(request, 'Registration done successfully')
            return render(request, 'pages/login/login.html')
# Logout Controller
def logout(request):
    del request.session['user_logged']
    return redirect('login')