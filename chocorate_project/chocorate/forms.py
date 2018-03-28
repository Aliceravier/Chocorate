from django import forms
from django.contrib.auth.models import User
from chocorate.models import UserProfile
from chocorate.models import Search
from chocorate.models import Chocolate
from chocorate.models import Comment
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Requires a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'notifications')

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
    picture_url = forms.CharField(max_length=200,
                                  help_text="Enter url of chocolate")
    picture_alt = forms.CharField(max_length=200,
                                  help_text="Enter written description for image here")
    class Meta:
        model = Chocolate
        fields = ('name', 'chocolate_type', 'description', 'picture','picture_url','picture_alt',)

class AddCommentForm(forms.ModelForm):
    message = forms.CharField(max_length=500,
                              help_text="Enter comment here")
    rating = forms.FloatField(help_text="Rating here")
    class Meta:
        model = Comment
        fields = ('message', 'rating')

class SettingsForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

