from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from website.choices import *
from datetime import datetime, date

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class NewUser(models.Model):
    username = models.CharField(max_length= 20)
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    email = models.CharField(max_length= 50)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.username + " - " + self.lastname


class Post(models.Model):
    user = models.ForeignKey(User)
    post = models.CharField(max_length=500, default='')
    gender = models.CharField(max_length=500, default='')
    dob = models.CharField(max_length=500, default='')
    phone = models.CharField(max_length=500, default='')
    address = models.CharField(max_length= 100, default='')
    state = models.CharField(max_length=500, default='')
    postcode = models.CharField(max_length=500, default='')
    userType = models.CharField(max_length=500, default='')
    # email = models.CharField(max_length= 50)