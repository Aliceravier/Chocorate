
from django import forms
from django.contrib.auth.models import User
from chocorate.models import UserProfile
from chocorate.models import Search


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