from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from candidates.models.EntryTest import *
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.PriorityDegree import *
from django.core import serializers
import json

def index(request):
    return render(request,'dashboard/entrytest/qualification.html')

def verifyQualification(request):
    if request.method == 'POST':

        action = request.POST['action']

        if action == '0':
            id = request.POST['id']
            obj = {
                'challan': None,
                'status': None
            }
            try:
                data = DegreePriorities.objects.get(candidate_id=id)
                obj = {
                    'challan': str(data.priority_form),
                    'status': data.form_status
                }
            except DegreePriorities.DoesNotExist:
                obj['status'] = -1
            return HttpResponse(json.dumps(obj), content_type="application/json", status=200)
        elif action == '1':
            id = request.POST['id']
            status = DegreePriorities.objects.filter(candidate_id=id).update(form_status = 1)
            if status:
                msg = "Challan Approved Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message': msg
            }), content_type='application/json', status=200)
        elif action == '2':
            id = request.POST['id']
            status = DegreePriorities.objects.filter(candidate_id=id).update(form_status=0)
            if status:
                msg = "Challan Rejected Successfully"
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
        " `candidates_candidateprofile`.`permanent_address` as paddress from `candidates_candidateprofile` INNER JOIN `candidates_degreepriorities` ON"
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