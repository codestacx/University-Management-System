from django.http import HttpResponse
from django.shortcuts import render,redirect
from candidates.models.EntryTest import *
import json
def result(request):
    if request.method == 'POST':
        queryset = AppliedCandidate.objects.raw(
            "SELECT `candidates_appliedcandidate`.`id`, `candidates_appliedcandidate`.`candidate_id`,"
            "`candidates_candidateprofile`.`firstname` as firstname, `candidates_candidateprofile`.`lastname` as lastname,"
            "`candidates_candidateprofile`.`cnic` as cnic, `candidates_degree`.`degree_name` , `candidates_degree`.`degree_level` as level,"
            "`candidates_testtypes`.`total_marks`,`candidates_testtypes`.`test_id` as testid FROM `candidates_appliedcandidate` INNER JOIN `candidates_candidateprofile` ON"
            "`candidates_appliedcandidate`.`candidate_id` = `candidates_candidateprofile`.`candidate_id`"
            "INNER JOIN `candidates_degree` ON `candidates_degree`.`degree_id` = `candidates_appliedcandidate`.`degree_id` "
            "INNER JOIN `candidates_testtypes` ON `candidates_appliedcandidate`.`degree_id` = `candidates_testtypes`.`degree_id`"
            "WHERE `candidates_appliedcandidate`.`challan_status`=1")
        objects = []
        for row in queryset:
            obj = {}
            obj['id'] = row.id;
            obj['candidate_id'] = row.candidate_id
            obj['cnic'] = row.cnic
            obj['name'] = str(row.firstname) + ' ' + str(row.lastname)
            obj['program'] =  str(row.level)+str(row.degree_name)
            obj['totalmarks'] = (row.total_marks)
            obj['testid'] = row.testid
            objects.append(obj)
        return HttpResponse(json.dumps(objects), content_type='application/json', status=200)
    else:
        return render(request,'dashboard/entrytest/entrytestresult.html')

def uploadResult(request):
    if request.method == 'POST':
        id = request.POST['candidate_id']
        action = request.POST['action']
        obj = {}
        if action == '0':

            try:
                res = AppliedCandidate.objects.get(candidate_id=id)
                try:
                    can = EntryTestResult.objects.get(candidate_id = id)
                    obj['status'] = 2
                    return HttpResponse(json.dumps(obj))
                except EntryTestResult.DoesNotExist:
                    degree_id = AppliedCandidate.objects.get(candidate_id=id).degree_id
                    testid = TestTypes.objects.get(degree_id=degree_id).test_id
                    obj['status'] = 0
                    #check for challan form
                    challan = AppliedCandidate.objects.get(candidate_id=id).challan_status
                    if challan == 0:
                        obj['status'] = -2
                        return HttpResponse(json.dumps(obj))
                    obj['testid']=testid
                    return HttpResponse(json.dumps(obj))
            except AppliedCandidate.DoesNotExist:
                obj['status'] = -1
            return HttpResponse(json.dumps(obj))
        else:
            marks = request.POST['marks']
            testid=request.POST['testid']
            status = EntryTestResult.objects.create(obtained_marks = marks,test_id=testid,candidate_id=id)
            obj = {}
            if status:
                obj['status'] = True
            else:
                obj['status'] = False
            return HttpResponse(json.dumps(obj),content_type='application/json',status=200)



    return HttpResponse('page not available')
