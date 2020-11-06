from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET(-1))
    address = models.CharField(max_length=255, null=False)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.user

class ProfileTwo(models.Model):
    profileModel = models.ForeignKey(Profile, on_delete = models.SET(-1))
    address = models.CharField(max_length=255, null=False)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return profileModel

class ProfileWeb(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    email = models.CharField(max_length=255, null=False)
 


