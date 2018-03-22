from django.shortcuts import render
from django.http import HttpResponse

from chocorate.forms import SearchForm
from chocorate.models import Search


def home(request):
    context_dict = {'current': 'home'}
    return render(request, 'chocorate/home.html', context = context_dict)

def categories(request):
    context_dict = {'current': 'categories'}
    return render(request, 'chocorate/categories.html', context = context_dict)

def profile(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/profile.html', context = context_dict)

def about(request):
    context_dict = {"current":"about"}
    return render(request, 'chocorate/about.html', context = context_dict)



def signUpIn(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/signUpIn.html', context = context_dict)

def myPost(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/myPost.html', context = context_dict)

def addPost(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/addPost.html', context = context_dict)

def settings(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/settings.html', context = context_dict)

def FAQ(request):
    context_dict = {"current":"about"}
    return render(request, 'chocorate/FAQ.html', context = context_dict)

def searchResults(request):
    context_dict = {}
    print (request.method)
    print (request.POST)
    if request.method == "POST":
        form = SearchForm(data = request.POST)
        #print ('form %s' % form.search)
        search_obj = form.save(commit=False)
        print (search_obj)
        context_dict['term'] = request.POST['search']
    return render(request, 'chocorate/results.html', context = context_dict)



