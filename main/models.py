from django.db import models
from django.db.models.fields import BooleanField

class ToDo(models.Model):
   text = models.CharField(max_length=100) 
   created_at = models.DateTimeField(auto_now_add=True)
   is_closed = models.BooleanField(default=False)
   is_favorite = models.BooleanField(default=False)



class ToMeet(models.Model):
    persone = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=40)
    date_of_meeting = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)