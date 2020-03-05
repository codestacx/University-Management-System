from django.db import models
from candidates.models.User import User

class MeritList(models.Model):
    candidate_id = models.ForeignKey(User,on_delete=models.CASCADE)
    program_selected = models.CharField(max_length=50)
    selection_status = models.IntegerField()

