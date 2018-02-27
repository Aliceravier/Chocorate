from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("New home")

def categories(request):
    return HttpResponse("Cats, all cats")

def profile(request):
    return HttpResponse("Hi you")

def about(request):
    return HttpResponse("What is this about?")



def signUpIn(request):
    return HttpResponse("Sign up/in")

def myPost(request):
    return HttpResponse("Add your post here")

def addPost(request):
    return HttpResponse("This... is your post")

def settings(request):
    return HttpResponse("Set the ings")

def FAQ(request):
    return HttpResponse("F ask questions")


