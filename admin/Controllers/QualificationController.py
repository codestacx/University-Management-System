from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from candidates.models.EntryTest import *
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.PriorityDegree import *
from candidates.models.Degree import *
from admin.Controllers.AuthController import require_login
import json


@require_login
def index(request):
    return render(request,'dashboard/entrytest/qualification.html')

def verifyQualification(request):
    if request.method == 'POST':
        action = request.POST['action']
        if action == '0':
            id = request.POST['id']
            obj = {

                'status': None
            }
            try:
                count = User.objects.filter(id=id).count()
                if count > 0:
                    # Unpaid Challan
                    if DegreePriorities.objects.get(candidate_id=id).form_status == 0:
                        return HttpResponse(json.dumps({
                            'status': -2
                        }))
                    #ALREADY APPROVED
                    if QualificationStatus.objects.get(candidate_id = id).status == 1:
                        return HttpResponse(json.dumps({
                            'status':1
                        }))


                    querySet = Qualification.objects.raw("SELECT  `candidates_qualification`.`id`,`candidates_qualification`.`candidate_id`,`candidates_qualification`.`total_marks`,"
                                                   "`candidates_qualification`.`obtained_marks`,`candidates_qualification`.`institute`,`candidates_qualification`.`passing_year`,"
                                                   "`candidates_degreecriteria`.`requirement` as requirement FROM `candidates_qualification` LEFT JOIN `candidates_degreecriteria` ON `candidates_degreecriteria`.`degree_criteria_id`=`candidates_qualification`.`criteria_id`")

                    userimage = CandidateProfile.objects.get(candidate_id=id).image

                    data = [{'id': row.id,
                             'candidate_id': row.candidate_id,
                             'totalmarks':row.total_marks,
                             'obtained':row.obtained_marks,
                             'institute':row.institute,
                             'passingyear':str(row.passing_year),
                             'requirement':row.requirement} for row in querySet]

                    obj = {
                        'result':data,
                        'status':0,
                        'image':str(userimage)
                    }
                    return HttpResponse(json.dumps(obj), content_type="application/json", status=200)
                else:
                    obj['status'] = -1
            except Qualification.DoesNotExist:
                obj['status'] = -1
            return HttpResponse(json.dumps(obj), content_type="application/json", status=200)
        elif action == '1':
            id = request.POST['id']
            status = QualificationStatus.objects.filter(candidate_id=id).update(status = 1)
            if status:
                msg = "Qualification Approved Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message': msg
            }), content_type='application/json', status=200)
        elif action == '2':
            id = request.POST['id']
            status = QualificationStatus.objects.filter(candidate_id=id).update(status=0)
            if status:
                msg = "Qualification Rejected Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message': msg
            }), content_type='application/json', status=200)
        elif action == '3':
            objects = []
            queryset = CandidateProfile.objects.raw(
        " SELECT "
        "`candidates_candidateprofile`.`id`,"        
        "`candidates_candidateprofile`.`candidate_id`,"
        "`candidates_candidateprofile`.`firstname` as firstname, "
        "`candidates_candidateprofile`.`lastname` as lastname," 
        "`candidates_candidateprofile`.`cnic` as cnic ,"
        " `candidates_candidateprofile`.`temporary_address` as taddress,"
        " `candidates_candidateprofile`.`permanent_address` as paddress from `candidates_candidateprofile` "
        "INNER JOIN `candidates_degreepriorities` ON"
                "`candidates_degreepriorities`.`candidate_id` = `candidates_candidateprofile`.`candidate_id`"
                "WHERE"
                "`candidates_degreepriorities`.`form_status`=1")
            for row in queryset:
                obj ={}

                obj['candidate_id'] = row.candidate_id
                obj['cnic'] = row.cnic
                obj['name'] = str(row.firstname) + ' ' + str(row.lastname)
                obj['taddress'] = row.taddress;
                obj['paddress'] = row.paddress;
                objects.append(obj)
            return HttpResponse(json.dumps(objects),content_type='application/json',status=200)
    return HttpResponse('working')