from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.mixins import PermissionRequiredMixin

class Member(models.Model):
    """Student or Prof."""
    id=0 #if id==0, unassigned member
    pw =models.CharField(max_length=20) #encoding 방법 추후 제작
    is_student= True
    name=models.CharField(max_length=20, help_text='Enter a Member\'s name')
    email=models.CharField(max_length=30,help_text='Enter your email')
    department=models.CharField(max_length=20,help_text='department')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this member."""
        return reverse('member-detail', args=[str(self.id)])

