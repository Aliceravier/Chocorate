from django.conf.urls import url
from chocorate import views

urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^about/$', views.about, name = 'about'),
    url(r'^categories/$', views.categories, name = 'categories'),
        
    url(r'^profile/signUpIn/$', views.signUpIn, name = 'signUpIn'),
    url(r'^profile/myPost/$', views.myPost, name = 'myPost'),
    url(r'^profile/addPost/$', views.addPost, name = 'addPost'),
    url(r'^profile/settings/$', views.settings, name = 'settings'),
    url(r'^about/FAQ/$', views.FAQ, name = 'FAQ'),
    
    ]
