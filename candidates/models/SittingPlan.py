from django.db import models
from candidates.models.User import User


#model containing information about Hall


class Hall(models.Model):
    hall_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    available_seats = models.IntegerField()
    location = models.TextField()


    class Meta:
        app_label = 'candidates'

# model containing information about the time slots


class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    seat_limits = models.IntegerField()

    class Meta:
        app_label = 'candidates'


# model containing all the info about sitting plan of particular candidate


class PlanInfo(models.Model):
    reg_number = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall,on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    class Meta:
        app_label = 'candidates'
