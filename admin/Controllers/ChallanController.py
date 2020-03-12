from django.http import HttpResponse
from django.shortcuts import render,redirect
from candidates.models.EntryTest import *
import json
def entryTestChallan(request):
    return render(request,'dashboard/entrytest/verifychallan.html')
def verifyEntryTestChallan(request):
    if request.method == 'POST':
        id = request.POST['id']
        action = request.POST['action']
        if action == 0:
            data = AppliedCandidate.objects.get(candidate_id = id)
            obj = {
                'challan':str(data.paid_challan_copy)
            }
            return HttpResponse(json.dumps(obj), content_type="application/json", status=200)
        else:
            status = AppliedCandidate.objects.filter(candidate_id=id).update(challan_status = 1)
            if status:
                msg = "Challan Approved Successfully"
            else:
                msg = "Sorry something goes wrong ..."
            return HttpResponse(json.dumps({
                'message':msg
            }),content_type='application/json',status=200)
    return HttpResponse('working')