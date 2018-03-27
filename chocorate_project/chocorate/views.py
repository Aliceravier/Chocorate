from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from chocorate.forms import SearchForm 
from chocorate.models import Search, Chocolate, UserProfile
from chocorate.forms import AddPostForm, SignUpForm, SettingsForm




def home(request):
    context_dict = {}
    context_dict['chocolates']=Chocolate.objects.order_by('name')
    context_dict['chocolates5']=Chocolate.objects.order_by('name')[:5]
    return render(request, 'chocorate/home.html', context=context_dict)

def categories(request):
    context_dict = {}
    types = ['milk', 'dark']
    all_chocs = []
    for t in types:
        chocolates = Chocolate.objects.filter(chocolate_type=t)
        chocolates = [c.name for c in chocolates]
        temp = [t]
        temp.extend(chocolates)
        print (temp)
        all_chocs.append(tuple(temp))

    context_dict['categories'] = all_chocs
    return render(request, 'chocorate/categories.html', context = context_dict)

def profile(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/profile.html', context = context_dict)

def about(request):
    context_dict = {"current":"about"}
    return render(request, 'chocorate/about.html', context = context_dict)



def signUp(request):
    sign_form = SignUpForm()
    if request.method == 'POST':
        sign_form = SignUpForm(request.POST)
        if sign_form.is_valid():
            user = sign_form.save()
            user.set_password(user.password)
            user.save()
            return home(request)
        else:
            print(sign_form.errors)
    return render(request, 'chocorate/signUp.html', {'form' : sign_form})

@login_required()
def signOut(request):
    logout(request)

@login_required()
def myPost(request):
    context_dict = {'current': 'profile'}
    return render(request, 'chocorate/myPost.html', context = context_dict)

@login_required()
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

@login_required
def settings(request):
    context_dict = {}

    print ('request method %s' % request.method)
    if request.method == 'POST':
        print (request.POST)
        passwordForm = PasswordChangeForm(request.user, request.POST)
        profileForm = SettingsForm(data=request.POST)

        print ('info %s' % profileForm)

        if profileForm.is_valid():
            profile = profileForm.save(commit=False)

        else:
            context_dict['profile_msg'] = profileForm.errors

        if passwordForm.is_valid():
            user = passwordForm.save()
            print ('user %s' % user)
            update_session_auth_hash(request, user)
            msg = 'Your password was successfully updated'
        else:
            msg = passwordForm.errors
        print ('method')

        context_dict['message'] = msg
    else:
        # settingsForm = SettingsForm(instance=request.user)
        # context_dict['settings_form'] = settingsForm
        context_dict['form'] = PasswordChangeForm(request.user)
        context_dict['settings_form'] = SettingsForm()


    return render(request, 'chocorate/settings.html', context_dict)


@login_required
def updateProfile(request):
    context_dict = {}

    print ('request method %s' % request.method)
    if request.method == 'POST':
        print (request.POST)
        profileForm = SettingsForm(data=request.POST)

        print ('info %s' % profileForm)

        if profileForm.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            print ('asd %s ' % request.POST['website'])
            print ('website-pre %s' % profile.website)

            profile.website = request.POST['website']
            profile.picture = request.POST['picture']
            profile.save()
            # profile.save(update_fields=['website', 'picture'])
            # profile = profileForm.save(commit=False)
            print ('profile %s' % profile)
            print ('website %s' % profile.website)
            context_dict['profile_msg'] = 'Successfully updated your profile'
        else:
            context_dict['profile_msg'] = profileForm.errors

    else:
        context_dict['form'] = SettingsForm()


    return render(request, 'chocorate/updateProfile.html', context_dict)

def FAQ(request):
    context_dict = {"current":"about"}
    return render(request, 'chocorate/FAQ.html', context=context_dict)

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
