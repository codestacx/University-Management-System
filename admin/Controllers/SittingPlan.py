from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from candidates.models.SittingPlan import *
from django.contrib import messages
def uploadHall(request):
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        capacity=request.POST['capacity']
        status = Hall.objects.create(title=title,location=location,available_seats=capacity)
        if status:
            messages.success(request,'Hall Information added successfully')
        else:
            messages.error(request,'Something goes wrong please try again....')
        return render(request,'dashboard/SittingPlan/UploadHall.html')
    return render(request,'dashboard/SittingPlan/UploadHall.html')

def uploadSlot(request):
    if request.method == 'POST':
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        limit=request.POST['limit']
        status = Slot.objects.create(start_time=start_time,end_time=end_time,seat_limits=limit)
        if status:
            messages.success(request,'Slot Information added successfully')
        else:
            messages.error(request,'Something goes wrong please try again....')
        return render(request,'dashboard/SittingPlan/UploadSlots.html')
    return render(request,'dashboard/SittingPlan/UploadSlots.html')