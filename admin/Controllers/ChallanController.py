from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.core import serializers
from candidates.models.EntryTest import *
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.PriorityDegree import *
from candidates.models.SittingPlan import *
from admin.Controllers.AuthController import require_login
import json


@require_login
def entryTestChallan(request):
    return render(request,'dashboard/entrytest/verify_entrytest_challans.html')

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

                # check if the user has uploaded challan
                if data.paid_challan_copy == '':
                    return HttpResponse(json.dumps({
                        'status':-2
                    }),content_type="application/json", status=200)

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
                
                rv = generate_sitting_plan(request.POST['id'])
                if rv == -1:
                    msg = "No seat available"
                elif rv == -2:
                    msg = "Seat already allocated"
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
  "`candidates_appliedcandidate`.`candidate_id` = `candidates_candidateprofile`.`candidate_id` WHERE `candidates_appliedcandidate`.`paid_challan_copy` != '' ")
            for row in queryset:
                obj ={}
                obj['id'] = row.id
                obj['candidate_id'] = row.candidate_id
                obj['cnic'] = row.cnic
                obj['name'] = str(row.firstname) + ' ' + str(row.lastname)
                obj['challan_status'] = row.challan_status
                obj['upload_challan_copy'] = str(row.paid_challan_copy)
                objects.append(obj)
            return HttpResponse(json.dumps(objects),content_type='application/json',status=200)
    return HttpResponse('working')


# TODO: if there are no halls and slots uploaded, break the application
def generate_sitting_plan(candidate_id):
    # get halls and slots
    halls = Hall.objects.all()
    slots = Slot.objects.all()
    candidate = User.objects.get(id=candidate_id)

    # check if candidate's sitting plan already generated
    if PlanInfo.objects.filter(candidate=candidate).exists():
        return -2

    for slot in slots:
        for hall in halls:
            seats = PlanInfo.objects.filter(slot=slot.slot_id, hall=hall.hall_id).order_by('seat_number')
            last_seat_number = None

            # no entry for this (slot, hall)
            if len(seats) == 0:
                last_seat_number = 0
            else:
                last_seat_number = seats.reverse()[0].seat_number

            if len(seats) < slot.seat_limits:
                x = PlanInfo.objects.create(candidate=candidate, slot=slot, hall=hall, seat_number=last_seat_number+1)
                return last_seat_number+1
    
    return -1

@require_login
def admissionChallan(request):
    return render(request, 'dashboard/entrytest/verify_admission_challans.html')


def verifyAdmissionChallan(request):
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

            queryset = DegreePriorities.objects.raw(
        "SELECT `candidates_degreepriorities`.`priority_id` , `candidates_degreepriorities`.`candidate_id` ,"
        "`candidates_degreepriorities`.`priority_form` as paid_challan_copy,"
        "`candidates_degreepriorities`.`form_status`  as challan_status, "
        "`candidates_candidateprofile`.`firstname` as firstname,  `candidates_candidateprofile`.`lastname` as lastname,"
        "`candidates_candidateprofile`.`cnic` as cnic FROM `candidates_degreepriorities`"
        " INNER JOIN"
    "`candidates_appliedcandidate` ON `candidates_appliedcandidate`.`candidate_id` = `candidates_degreepriorities`.`candidate_id`"
    "INNER JOIN `candidates_candidateprofile` ON `candidates_appliedcandidate`.`candidate_id` = `candidates_candidateprofile`.`candidate_id`")
            for row in queryset:
                obj ={}
                obj['id'] = row.priority_id
                obj['candidate_id'] = row.candidate_id
                obj['cnic'] = row.cnic
                obj['name'] = str(row.firstname) + ' ' + str(row.lastname)
                obj['challan_status'] = row.challan_status
                obj['upload_challan_copy'] = str(row.paid_challan_copy)
                objects.append(obj)
            return HttpResponse(json.dumps(objects),content_type='application/json',status=200)
    return HttpResponse('working')
