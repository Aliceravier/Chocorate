
from django import forms
from django.contrib.auth.models import User
from chocorate.models import UserProfile
from chocorate.models import Search
from chocorate.models import Chocolate


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class SearchForm(forms.ModelForm):

    search = forms.CharField(help_text="What are you looking for?")

    class Meta:
        model = Search
        fields = ('search',)

class AddPostForm(forms.ModelForm):
    name = forms.CharField(max_length=200,
                            help_text="Enter title for post")
    chocolate_type = forms.CharField(max_length=200,
                            help_text="Enter type of chocolate")
    description = forms.CharField(max_length=200,
                            help_text="Enter description for chocolate")
    picture = forms.ImageField(required=False, help_text="Upload image of chocolate here")
    class Meta:
        model = Chocolate
        fields = ('name', 'chocolate_type', 'description', 'picture',)
