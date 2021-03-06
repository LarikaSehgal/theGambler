"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('casino.urls')),
    path('casino/', include('casino.urls')),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='casino/index.html'),name='logout'),
    path('play/',user_views.play, name='play'),
    path('check/',user_views.checkans, name='check'),
    path('placebid/',user_views.placebid, name='placebid'),
    path('placebid_guessno/',user_views.placebid_guessno, name='placebid_guessno'),
    path('guessno/',user_views.guessno, name='guessno'),
    path('checknumber/',user_views.checknumber, name='checknumber'),
    #Edit user_view.profile to user_view.queryi here and create functions in user/views.py
    path('profile/query1a',user_views.query1a, name='query1a'),
    path('profile/query2a',user_views.query2a, name='query2a'),
    path('profile/query3a',user_views.query3a, name='query3a'),
    path('profile/query4a',user_views.query4a, name='query4a'),
    path('profile/query5a',user_views.query5a, name='query5a'),
    path('profile/query6a',user_views.query6a, name='query6a'),
    path('profile/query7a',user_views.query7a, name='query7a'),
    path('profile/query8a',user_views.query8a, name='query8a'),
    path('profile/query9a',user_views.query9a, name='query9a'),
    path('profile/query10a',user_views.query10a, name='query10a'),
    path('profile/query11a',user_views.query11a, name='query11a'),
    path('profile/query12a',user_views.query12a, name='query12a'),
]
