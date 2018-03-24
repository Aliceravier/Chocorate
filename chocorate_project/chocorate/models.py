from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
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
    picture_url = models.CharField(max_length=200)
    picture_alt = models.CharField(default="some image should be here", max_length=200)
    description = models.CharField(default="",max_length=200)

    def __str__(self):
        return self.name

#to add to comment class
class Rating(models.Model):
    chocolate=models.ForeignKey(Chocolate)
    
class Comment(models.Model):
    message = models.CharField(max_length=500, default="")
    rating = models.FloatField(default=2.5)
