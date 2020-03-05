from django.shortcuts import render,redirect,get_object_or_404
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

        try:
            user = User.objects.get(email=email,password=password,role=role)
            request.session['user_logged'] = True
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['isComplete'] = user.isComplete

            return redirect('index')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return render(request, 'pages/login/login.html')
    else:
        return render(request,'pages/login/login.html')



#sign up

def signup(request):
    if request.method=='POST':
        email = request.POST['mail']
        password = request.POST['password']
        status = User.objects.create(email=email,password=password,role='candidate')
        if (status):
            request.session['user_logged'] = True
            request.session['user_id']     = status.pk
            request.session['user_email']  = email

            messages.success(request, 'Registration done successfully')
            return render(request, 'pages/login/login.html')
# Logout Controller
def logout(request):
    del request.session['user_logged']
    return redirect('login')