from django.db import models
from candidates.models.User import User
from candidates.models.Degree import Degree


class AppliedTestCandidate(models.Model):
    candidate         = models.ForeignKey('User', on_delete=models.CASCADE)
    degree            = models.ForeignKey('Degree', null=True, on_delete=models.CASCADE)
    paid_challan_copy = models.ImageField('Image', upload_to='candidates/uploads/paid_challans')

    class Meta:
        app_label = 'candidates'

    def __str__(self):
        return f"candidate_id: {self.candidate} degree_id: {self.degree}"
