from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from rest_framework.authtoken.models import Token
from django.urls import reverse


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this member."""
        return reverse('member-detail', args=[str(self.id)])

