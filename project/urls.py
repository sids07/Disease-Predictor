"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from htmlcss import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('index.html/', views.home, name='index.html'),
    path('register.html/',views.register ,name='register.html'),
    path('new.html/', views.new, name='new.html'),
    path('login.html/', views.login, name='login.html'),
    # path('choose.html/', views.choose, name='choose.html'),
    # path('choosereg.html/', views.choosereg, name='chooseregister.html'),

]