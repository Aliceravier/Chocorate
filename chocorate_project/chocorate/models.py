from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    password = models.CharField(max_length=30)
    notifications = models.IntegerField()

    def __str__(self):
        return self.user.username

class Search(models.Model):
    search = models.CharField(max_length=128)

class Chocolate(models.Model):
    avgrating = models.FloatField()
    comments = models.TextField()
    name = models.CharField(max_length=30)
    # url = models.URLField()
    picture = models.ImageField()
    description = models.CharField(max_length=200)