from django.db import models
from candidates.models.User import User


class CandidateProfile(models.Model):
    firstname         = models.CharField('firstname',max_length=50,blank= False)
    lastname          = models.CharField('lastname',blank=False,max_length=50)
    cnic              = models.CharField('cnic',blank = False,max_length=13)
    temporary_address = models.CharField('temporary_address', max_length = 255)
    permanent_address = models.CharField('permanent_address', max_length = 255)
    phone             = models.CharField('phone', max_length=30)
    image             = models.ImageField('Image',upload_to='candidates/')

    # forein key one-to-one User
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        app_label = 'candidates'

    def __str__(self):
        return (str(self.id))

    def registerUser(firstname ,
                lastname ,
                phone ,
                cnic ,
                image ,
                temporary_address,
                permanent_address ,
                candidate_id
                ):
        status = CandidateProfile.objects.create(
            firstname=firstname, lastname  = lastname,
            phone     = phone,
            cnic      = cnic,
            image     = image,
            temporary_address = temporary_address,
            permanent_address = permanent_address,
            candidate_id = candidate_id
        )

        return status

    def updateUser(firstname ,
                lastname ,
                phone ,
                cnic ,
                image ,
                temporary_address,
                permanent_address ,
                candidate_id
                ):

        data = CandidateProfile.objects.get(candidate_id=candidate_id)
        data.firstname = firstname
        data.lastname = lastname
        data.cnic = cnic
        data.temporary_address = temporary_address
        data.permanent_address = permanent_address
        data.phone = phone
        data.save()
