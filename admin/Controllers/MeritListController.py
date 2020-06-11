from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from candidates.models.CandidateProfile import CandidateProfile

def meritlists_bachelor(request):
    query = "SELECT 1 as id,   `candidates_candidateprofile`.`firstname`,`candidates_candidateprofile`.`id` as cid, `candidates_candidateprofile`.`lastname`, " \
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
            "ON `candidates_candidateprofile`.`candidate_id` = `candidates_qualificationstatus`.`candidate_id`"

    data = CandidateProfile.objects.raw(query)
    return render(request,'dashboard/meritlists/bachelor.html',{'candidates':data})


def meritlists_mphill(request):
    query = "SELECT 1 as id,   `candidates_candidateprofile`.`firstname`,`candidates_candidateprofile`.`id` as cid, `candidates_candidateprofile`.`lastname`, " \
            "`candidates_qualificationstatus`.`candidate_id` as candidate_id ," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification` " \
            "WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=3 AND `candidates_qualification`.`degree_id`=2 )  " \
            "as matric," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=4 AND `candidates_qualification`.`degree_id`=2 )  as intermediate," \
            "(SELECT `candidates_qualification`.`obtained_marks` FROM `candidates_qualification`" \
            " WHERE `candidates_qualification`.`candidate_id`=`candidates_qualificationstatus`.`candidate_id` " \
            "AND `candidates_qualification`.`criteria_id`=5 AND `candidates_qualification`.`degree_id`=2 )  as bachelor," \
            "(SELECT `candidates_entrytestresult`.`obtained_marks` FROM `candidates_entrytestresult` WHERE " \
            "`candidates_entrytestresult`.`candidate_id`= `candidates_qualificationstatus`.`candidate_id`) as entry " \
            "FROM `candidates_qualificationstatus` INNER JOIN `candidates_candidateprofile` " \
            "ON `candidates_candidateprofile`.`candidate_id` = `candidates_qualificationstatus`.`candidate_id`"

    data = CandidateProfile.objects.raw(query)
    return render(request, 'dashboard/meritlists/bachelor.html', {'candidates': data})
