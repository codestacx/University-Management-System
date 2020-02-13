from django.shortcuts import render,redirect
from django.http import HttpResponse
#import all models
from candidates.models.User import User
#flash messages
from django.contrib import messages

def index(request):
    if request.session.has_key('user_logged'):
        return render(request,'pages/home/index.html')
    else:
        return redirect('login')