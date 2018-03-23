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
    avgrating = models.FloatField(default=2.5)
    comments = models.TextField(default="")
    name = models.CharField(default="",max_length=30)
    chocolate_type = models.CharField(default="", max_length=200)
    # url = models.URLField()
    picture = models.ImageField(blank=True, null=True, help_text="Upload image of chocolate here")
    description = models.CharField(default="",max_length=200)
    

class Rating(models.Model):
    chocolate=models.ForeignKey(Chocolate)
