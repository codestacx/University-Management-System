from django.http import HttpResponse
from django.shortcuts import render, redirect
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.User import User
from candidates.models.Rejection import Rejection
from admin.Controllers.AuthController import require_login
from django.shortcuts import reverse
from django.contrib import messages


@require_login
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@require_login
def verify_candidate_profile(request):
    if request.method == 'POST':
        id = request.POST['id']
        return HttpResponse(str(id))
    elif request.method == 'GET':
       # candidates = CandidateProfile.objects.all()
        candidates = User.objects.raw("SELECT `candidates_candidateprofile`.`firstname`, `candidates_candidateprofile`.`lastname`, "
                                      "`candidates_candidateprofile`.`cnic`,`candidates_candidateprofile`.`image`,"
                                      "`candidates_user`.`active`,`candidates_user`.`id` FROM `candidates_user` "
                                      "INNER JOIN `candidates_candidateprofile` ON "
                                      "`candidates_candidateprofile`.`candidate_id`=`candidates_user`.`id`")
        return render(request, 'dashboard/candidates/verify_candidate_profiles.html', {'candidates':candidates})


def deactivate_candidate(request,id):
    messages.success(request,'User Deactivated Successfully')
    User.objects.filter(id=id).update(active=0)

    return redirect(reverse('verify_candidate_profile'))

def activate_candidate(request,id):
    messages.success(request,'User Activated Successfully')
    User.objects.filter(id=id).update(active=1)
    return redirect(reverse('verify_candidate_profile'))

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
