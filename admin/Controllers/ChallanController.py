from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from candidates.models.EntryTest import *
from candidates.models.CandidateProfile import CandidateProfile
from django.core import serializers
import json
def entryTestChallan(request):
    return render(request,'dashboard/entrytest/verifychallan.html')
def verifyEntryTestChallan(request):
    if request.method == 'POST':

        action = request.POST['action']

        if action == '0':
            id = request.POST['id']
            obj = {
                'challan': None,
                'status': None
            }
            try:
                data = AppliedCandidate.objects.get(candidate_id=id)
                obj = {
                    'challan': str(data.paid_challan_copy),
                    'status': data.challan_status
                }
            except AppliedCandidate.DoesNotExist:
                obj['status'] = -1
            return HttpResponse(json.dumps(obj), content_type="application/json", status=200)
        elif action == '1':
            id = request.POST['id']
            status = AppliedCandidate.objects.filter(candidate_id=id).update(challan_status = 1)
            if status:
                msg = "Challan Approved Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message': msg
            }), content_type='application/json', status=200)
        elif action == '2':
            id = request.POST['id']
            status = AppliedCandidate.objects.filter(candidate_id=id).update(challan_status=0)
            if status:
                msg = "Challan Rejected Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message': msg
            }), content_type='application/json', status=200)
        elif action == '3':
            objects = []
            queryset = AppliedCandidate.objects.raw(
        "SELECT  `candidates_appliedcandidate`.`id` , `candidates_appliedcandidate`.`candidate_id` , `candidates_candidateprofile`.`firstname` as firstname,  `candidates_candidateprofile`.`lastname` as lastname,`candidates_candidateprofile`.`cnic` as cnic,`candidates_appliedcandidate`.`paid_challan_copy` as paid_challan_copy,`candidates_appliedcandidate`.`challan_status` as challan_status FROM `candidates_appliedcandidate` INNER JOIN `candidates_candidateprofile` ON "
  "`candidates_appliedcandidate`.`candidate_id` = `candidates_candidateprofile`.`candidate_id`")
            for row in queryset:
                obj ={}
                obj['id'] = row.id;
                obj['candidate_id'] = row.candidate_id
                obj['cnic'] = row.cnic
                obj['name'] = str(row.firstname) + ' ' + str(row.lastname)
                obj['challan_status'] = row.challan_status
                obj['upload_challan_copy'] = str(row.paid_challan_copy)
                objects.append(obj)
            return HttpResponse(json.dumps(objects),content_type='application/json',status=200)
    return HttpResponse('working')