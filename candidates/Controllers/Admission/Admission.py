from django.http import HttpResponse
from django.shortcuts import render,redirect
from candidates.models.PriorityDegree import *
from candidates.models.EntryTest import *
from candidates.models.Degree import *
from candidates.models.CandidateProfile import *
from django.contrib import messages
import string
def index(request):
    user_id = request.session['user_id']
    if request.method == 'POST':
        priorities_list = request.POST.getlist('priority_unit[]')
        program_list = request.POST.getlist('program_unit[]')
        zipped = zip(priorities_list,program_list)

        zipped_list =  list(zipped)
        res = sorted(zipped_list, key=lambda x: x[0])
        num2alpha = dict(zip(range(1, 12), string.ascii_lowercase))
        #save priorities
        d = DegreePriorities()
        d.candidate_id = user_id
        for x,y in ((res)):
            field = 'priority_' +num2alpha[int(x)]
            setattr(d, field, y)
        d.save()

        objects = []
        degree_id = request.POST['degree_id']
        degree_level = request.POST['degree_level']
        matric_institute = request.POST['matric_institute']
        matric_total_marks = request.POST['matric_total_marks']
        matric_obtained_marks = request.POST['matric_obtained_marks']
        passing_year = request.POST['matric_py']


        objects.append(
            Qualification(total_marks=matric_total_marks,
                            obtained_marks=matric_obtained_marks,
                            institute=matric_institute,
                            candidate_id=user_id,
                            degree_id=degree_id,
                            passing_year = passing_year,
                            criteria_id=DegreeCriteria.objects.filter(requirement='Matric', degree_id=degree_id)[
                                0].degree_criteria_id)
        )


        inter_institute = request.POST['inter_institute']
        inter_total_marks = request.POST['inter_total_marks']
        inter_obtained_marks = request.POST['inter_obtained_marks']
        passing_year = request.POST['inter_py']

        objects.append(
            Qualification(total_marks=inter_total_marks,
                          obtained_marks=inter_obtained_marks,
                          institute=inter_institute,
                          candidate_id=user_id,
                          degree_id=degree_id,
                          passing_year = passing_year,
                          criteria_id=DegreeCriteria.objects.filter(requirement='Interemediate', degree_id=degree_id)[
                              0].degree_criteria_id)
        )


        if degree_level == 'MPhill':
            bs_institute = request.POST['bs_institute']
            bs_total_marks = 4
            bs_obtained_marks = request.POST['bs_obtained_marks']
            passing_year = request.POST['bs_py']

            objects.append(
                Qualification(total_marks=bs_total_marks,
                              obtained_marks=bs_obtained_marks,
                              institute=bs_institute,
                              candidate_id=user_id,
                              degree_id=degree_id,
                              passing_year = passing_year,
                              criteria_id=DegreeCriteria.objects.filter(requirement='BS', degree_id=degree_id)[
                                  0].degree_criteria_id)
            )





        elif degree_level == 'Phd':
            bs_institute = request.POST['bs_institute']
            bs_total_marks = 4
            bs_obtained_marks = request.POST['bs_obtained_marks']
            passing_year = request.POST['bs_py']

            objects.append(
                Qualification(total_marks=bs_total_marks,
                              obtained_marks=bs_obtained_marks,
                              institute=bs_institute,
                              candidate_id=user_id,
                              degree_id=degree_id,
                              passing_year = passing_year,
                              criteria_id=DegreeCriteria.objects.filter(requirement='BS', degree_id=degree_id)[
                                  0].degree_criteria_id)
            )

            mphill_institute = request.POST['mphill_institute']
            mphill_total_marks = 4
            mphill_obtained_marks = request.POST['mphill_obtained_marks']
            passing_year = request.POST['mphill_py']

            objects.append(
                Qualification(total_marks=mphill_total_marks,
                              obtained_marks=mphill_obtained_marks,
                              institute=mphill_institute,
                              candidate_id=user_id,
                              degree_id=degree_id,
                              passing_year=passing_year,
                              criteria_id=DegreeCriteria.objects.filter(requirement='Mphill', degree_id=degree_id)[
                                  0].degree_criteria_id)
            )


        status = Qualification.objects.bulk_create(objects)
        return HttpResponse(str(len(objects)))
    try:
        degree_id = AppliedCandidate.objects.get(candidate_id=user_id).degree_id
        degree_level = Degree.objects.get(degree_id=degree_id).degree_level
        degree_criteria = DegreeCriteria.objects.filter(degree_id=degree_id).all()
        degrees = PrioriyDegree.objects.all()
        priorities = []
        for i in range(1, 13):
            priorities.append(i)
        return render(request, 'pages/admission/admission-application.html',
                      {'degree_id':degree_id,
                       'degree_level':degree_level,
                       'degree_criteria':degree_criteria,
                       'degrees': degrees, 'priorities': priorities
                       })
    except AppliedCandidate.DoesNotExist:
        return HttpResponse("no result found")



def getChallan(request):
    user_id = request.session['user_id']
    if request.method=='POST':

        if request.FILES:
            obj = DegreePriorities.objects.get(candidate_id=user_id)
            obj.priority_form=request.FILES['paid-challan-copy']
            obj.save()
            return render(request, 'pages/admission/challan.html')


    try:
        status = DegreePriorities.objects.get(candidate_id=user_id)
        user = CandidateProfile.objects.get(candidate_id=user_id)
        return render(request,'pages/admission/challan.html',{'context':status,'user':user})
    except DegreePriorities.DoesNotExist:
        messages.error(request,'No challan available')
        return render(request,'pages/admission/challan.html')

def finalizeAdmission(request):
    return render(request,'pages/admission/finalize-admission.html')

def meritListStatus(request):
    return render(request,'pages/admission/merit-list-status.html')


