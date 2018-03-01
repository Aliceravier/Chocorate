from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict = {'current': 'home'}
    return render(request, 'chocorate/home.html', context = context_dict)

def categories(request):
    context_dict = {}
    return render(request, 'chocorate/categories.html', context = context_dict)

def profile(request):
    context_dict = {}
    return render(request, 'chocorate/profile.html', context = context_dict)

def about(request):
    context_dict = {"current":"about"}
    return render(request, 'chocorate/about.html', context = context_dict)



def signUpIn(request):
    context_dict = {}
    return render(request, 'chocorate/signUpIn.html', context = context_dict)

def myPost(request):
    context_dict = {}
    return render(request, 'chocorate/myPost.html', context = context_dict)

def addPost(request):
    context_dict = {}
    return render(request, 'chocorate/addPost.html', context = context_dict)

def settings(request):
    context_dict = {}
    return render(request, 'chocorate/settings.html', context = context_dict)

def FAQ(request):
    context_dict = {}
    return render(request, 'chocorate/FAQ.html', context = context_dict)


