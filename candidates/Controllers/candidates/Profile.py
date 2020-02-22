from django.shortcuts import render
from django.http import HttpResponse
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.User import  User
from django.contrib import messages
import var_dump
def personalInfo(request):
    user_id = request.session['user_id']
    if request.method  == 'POST':
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        contact   = request.POST['contact']
        cnic      = request.POST['cnic']
        image     = request.FILES['profile_avatar']
        permanent_address = request.POST['permanent_address']
        temporary_address = request.POST['temporary_address']
        isUpdate = request.POST['status']

        if isUpdate == '1':
            old_picture = request.POST['old_picture'];
            status = CandidateProfile.updateUser(firstname=firstname,
                                                   lastname=lastname,
                                                   phone=contact,
                                                   cnic=cnic,
                                                   image=image,
                                                   temporary_address=temporary_address,
                                                   permanent_address=permanent_address,
                                                   candidate_id=user_id)

        else:
            status  = CandidateProfile.registerUser(firstname=firstname,
                                        lastname=lastname,
                                        phone=contact,
                                        cnic=cnic,
                                        image=image,
                                        temporary_address=temporary_address,
                                        permanent_address=permanent_address,
                                        candidate_id=user_id)
            rows = User.objects.filter(id=user_id).update(isComplete=1)
        if status:
            request.session['isComplete'] = 1
            messages.success(request,'Profile Updated Successfully.....')
            return render(request,'pages/home/index.html')
        #return HttpResponse(firstname + ' ' + lastname + ' '+ contact + ' ' + cnic+'\n'+image+' '+permanent_address + ' '+temporary_address)
    elif request.session['isComplete'] == 1:
        # candidate = CandidateProfile.objects.raw("SELECT * FROM `candidates_user` INNER JOIN `candidates_candidateprofile`"
        # "ON `candidates_user`.`id`=`candidates_candidateprofile`.`candidate_id` WHERE `candidates_user`.`id`=%s",[user_id])

        widget = getProfileMetaData(user_id)
        profile = getProfileMetaData(user_id,True)

        return render(request,'pages/profile/personalinfo.html',{'profile':profile,'widget':widget})
    return render(request,'pages/profile/personalinfo.html')


def passwordInfo(request):
    user_id = request.session['user_id']
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        new_cpassword = request.POST['new_cpassword']

        obj = User.objects.get(id=user_id)

        if(obj.password != current_password):
            msg = "Current password is not current"
        elif new_password != new_cpassword:
            msg = "Password doesn't match"
        else:
            obj.password = new_password
            obj.save()
            msg = "password updated successfully"


        messages.success(request,msg)


    if request.session['isComplete'] == 1:
        widget = getProfileMetaData(user_id)
        return render(request,'pages/profile/change-password.html',{'widget':widget})
    return render(request, 'pages/profile/change-password.html')

def getProfileMetaData(user_id,isProfile=False):
    candidate = CandidateProfile.objects.raw("SELECT * FROM `candidates_user` INNER JOIN `candidates_candidateprofile`"
                                             "ON `candidates_user`.`id`=`candidates_candidateprofile`.`candidate_id` WHERE `candidates_user`.`id`=%s",
                                             [user_id])

    if not isProfile:
        data = {
        'email': candidate[0].email,
        'contact': candidate[0].phone,
        'name': candidate[0].firstname + ' ' + candidate[0].lastname,
        'location': candidate[0].permanent_address,
        'image': candidate[0].image,
        'status': candidate[0].isComplete
    }

    else:
        data = {
        'email': candidate[0].email,
        'contact': candidate[0].phone,
        'fname': candidate[0].firstname,
        'lname': candidate[0].lastname,
        'perm_address': candidate[0].permanent_address,
        'temp_address': candidate[0].temporary_address,
        'status': candidate[0].isComplete,
        'cnic': candidate[0].cnic,
        'phone': candidate[0].phone,
        'image': candidate[0].image

    }

    return data
