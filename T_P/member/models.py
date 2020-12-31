from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse





    
User                = get_user_model()

class Author(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class Register_Model(models.Model):
    author               = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name           = models.CharField(max_length=120)
    last_name            = models.CharField(max_length=120)
    Enrollment_No        = models.CharField(max_length=120)
    Ph_No                = models.CharField(max_length=120)
    CGPA                 = models.CharField(max_length=120)
    Percentage_in_10th   = models.CharField(max_length=120)
    Percentage_in_12th   = models.CharField(max_length=120)
    Branch               = models.CharField(max_length=120)
    Semester             = models.IntegerField()
    Batch                = models.CharField(max_length=120)
    Email                = models.EmailField()
    


    def __str__(self):
        return self.first_name