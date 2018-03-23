from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

from chocorate.forms import SearchForm 
from chocorate.models import Search, Chocolate
from chocorate.forms import AddPostForm, SignUpForm




def home(request):
    context_dict = {'current': 'home'}
    context_dict['chocolates']=Chocolate.objects.order_by('name')
    context_dict['chocolates5']=Chocolate.objects.order_by('name')[:5]
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
    sign_form = SignUpForm()
    if request.method == 'POST':
        sign_form = SignUpForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save(commit=True)
            user.save()
            return home(request)
        else:
            print(sign_form.errors)
    return render(request, 'chocorate/signUpIn.html', {'form' : sign_form})

def signOut(request):
    logout(request)

def myPost(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/myPost.html', context = context_dict)

def addPost(request):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            chocolate = form.save(commit=True)
            chocolate.save()
            return home(request)
        else:
            print(form.errors)
    return render(request, 'chocorate/addPost.html', {'form' : form})

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
        search_form = SearchForm(data = request.POST)
        #print ('form %s' % form.search)
        search_obj = search_form.save(commit=False)
        print (search_obj)
        context_dict['term'] = request.POST['search']
    return render(request, 'chocorate/results.html', context = context_dict)

def test(request):
    return render(request, 'chocorate/test.html')
