from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"