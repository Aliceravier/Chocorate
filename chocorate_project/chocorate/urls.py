from django.conf.urls import url
from chocorate import views
from django.contrib.auth.views import logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^results/$', views.searchResults, name='results'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^about/$', views.about, name='about'),
    url(r'^categories/$', views.categories, name='categories'),

    url(r'^profile/signUp/$', views.signUp, name='signUp'),
    url(r'^profile/login/$', auth_views.login,{'template_name': 'chocorate/login.html'}, name='login'),
    url(r'^profile/signOut/$', auth_views.logout,{'next_page': '/chocorate/home/'},  name='signOut'),
    url(r'^profile/myPost/$', views.myPost, name='myPost'),
    url(r'^profile/addPost/$', views.addPost, name='addPost'),
    url(r'^profile/changePassword/$', views.settings, name='changePassword'),
    url(r'^profile/updateProfile/$', views.updateProfile, name='updateProfile'),
    url(r'^about/FAQ/$', views.FAQ, name='FAQ'),
    url(r'^test/$', views.test, name='test'),

]
