from django.shortcuts import render
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile

def entry_test_application(request):
    context = {}
    context['degrees'] = Degree.objects.all()
    context['current_user'] = CandidateProfile.objects.filter(id=request.session['user_id'])
    return render(request, "pages/entrytest/entry_test_application.html", context=context)

def registeration_slip(request):
    return render(request, "pages/entrytest/registeration_slip.html")

def adjust_test_schedule(request):
    return render(request, "pages/entrytest/adjust_test_schedule.html")

def entry_test_result(request):
    return render(request, "pages/entrytest/entry_test_result.html")