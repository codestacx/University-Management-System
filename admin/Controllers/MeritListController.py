from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from candidates.models.CandidateProfile import CandidateProfile

def meritlists_bachelor(request):
    query = "SELECT 1 as id, `candidates_agreegat`.`total` as aggregate,  `candidates_candidateprofile`.`firstname`,`candidates_candidateprofile`.`id` as cid, `candidates_candidateprofile`.`lastname`, " \
            "`candidates_qualificationstatus`.`candidate_id` as candidate_id ," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=1 AND `candidates_qualification`.`degree_id`=1 )  " \
            "as matric,(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=2 AND `candidates_qualification`.`degree_id`=1 )  as intermediate," \
            "(SELECT `candidates_entrytestresult`.`obtained_marks` FROM `candidates_entrytestresult` WHERE " \
            "`candidates_entrytestresult`.`candidate_id`= `candidates_qualificationstatus`.`candidate_id`) as entry " \
            "FROM `candidates_qualificationstatus` INNER JOIN `candidates_candidateprofile` " \
            "ON `candidates_candidateprofile`.`candidate_id` = `candidates_qualificationstatus`.`candidate_id` LEFT JOIN `candidates_appliedcandidate` ON " \
            "`candidates_appliedcandidate`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` LEFT JOIN  `candidates_agreegat` ON `candidates_agreegat`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id`" \
            "WHERE `candidates_appliedcandidate`.`degree_id`=1"

    data = CandidateProfile.objects.raw(query)
    return render(request,'dashboard/meritlists/bachelor.html',{'candidates':data})


def meritlists_mphill(request):
    query = "SELECT 1 as id, `candidates_agreegat`.`total` as aggregate, `candidates_candidateprofile`.`firstname`, `candidates_candidateprofile`.`lastname`," \
            " `candidates_qualificationstatus`.`candidate_id` as candidate_id , " \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` AND " \
            "`candidates_qualification`.`criteria_id`=3 AND " \
            "`candidates_qualification`.`degree_id`=2 )  as matric," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=4 AND `candidates_qualification`.`degree_id`=2 ) " \
            " as intermediate," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=5 AND `candidates_qualification`.`degree_id`=2 )  as bs, " \
            "(SELECT `candidates_entrytestresult`.`obtained_marks` FROM `candidates_entrytestresult` " \
            "WHERE `candidates_entrytestresult`.`candidate_id`= `candidates_qualificationstatus`.`candidate_id`) as entry " \
            "FROM `candidates_qualificationstatus` " \
            "INNER JOIN `candidates_candidateprofile` ON " \
            "`candidates_candidateprofile`.`candidate_id` = `candidates_qualificationstatus`.`candidate_id` " \
            "LEFT JOIN `candidates_appliedcandidate` ON " \
            "`candidates_appliedcandidate`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "LEFT JOIN  `candidates_agreegat` " \
            "ON `candidates_agreegat`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id`" \
            "WHERE `candidates_appliedcandidate`.`degree_id`=2"

    data = CandidateProfile.objects.raw(query)
    return render(request, 'dashboard/meritlists/mphill.html', {'candidates': data})


def meritlists_phd(request):
    query = "SELECT 1 as id, `candidates_agreegat`.`total` as aggregate, `candidates_candidateprofile`.`firstname`, `candidates_candidateprofile`.`lastname`," \
            " `candidates_qualificationstatus`.`candidate_id` as candidate_id , " \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` AND " \
            "`candidates_qualification`.`criteria_id`=6 AND " \
            "`candidates_qualification`.`degree_id`=3 )  as matric," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=7 AND `candidates_qualification`.`degree_id`=3 ) " \
            " as intermediate," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=8 AND `candidates_qualification`.`degree_id`=3 )  as bs, " \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=9 AND `candidates_qualification`.`degree_id`=3 )  as mphill, " \
            "(SELECT `candidates_entrytestresult`.`obtained_marks` FROM `candidates_entrytestresult` " \
            "WHERE `candidates_entrytestresult`.`candidate_id`= `candidates_qualificationstatus`.`candidate_id`) as entry " \
            "FROM `candidates_qualificationstatus` " \
            "INNER JOIN `candidates_candidateprofile` ON " \
            "`candidates_candidateprofile`.`candidate_id` = `candidates_qualificationstatus`.`candidate_id` " \
            "LEFT JOIN `candidates_appliedcandidate` ON " \
            "`candidates_appliedcandidate`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "LEFT JOIN  `candidates_agreegat` ON " \
            "`candidates_agreegat`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id`" \
            "WHERE `candidates_appliedcandidate`.`degree_id`=3"

    data = CandidateProfile.objects.raw(query)
    return render(request, 'dashboard/meritlists/phd.html', {'candidates': data})

def calculator(request):
        return render(request,'dashboard/meritlists/meritcalculator.html')