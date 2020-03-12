from django.http import HttpResponse
from django.shortcuts import render,redirect
from candidates.models.User import User

def removeStudent(request):
    id = request.POST['id']
    return HttpResponse(str(id))