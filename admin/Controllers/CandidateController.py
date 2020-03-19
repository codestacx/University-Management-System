from django.http import HttpResponse
from django.shortcuts import render,redirect
from candidates.models.User import User
from candidates.models.Rejection import Rejection

def removeStudent(request):
    id = request.POST['id']
    return HttpResponse(str(id))

def rejection_reason(request):
    if request.method == 'POST':
        candidate_id = request.POST['candidate_id']
        category = request.POST['category']
        if Rejection.objects.filter(candidate_id=request.POST['candidate_id'], category='entrytest').exists():
            rejection = Rejection.objects.get(
                candidate_id=candidate_id,
                category=category
            )
            rejection.reason = request.POST['reason']
            rejection.save()
            return HttpResponse('updated')
        else:
            rejection = Rejection.objects.create(
                candidate_id=candidate_id,
                reason=request.POST['reason'],
                category=category
            )
            rejection.save()
            return HttpResponse('saved')
        return HttpResponse('something went wrong')
    else:
        return HttpResponse('Only POST supported')