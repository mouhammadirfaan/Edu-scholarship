from django.contrib import admin
from django.urls import path
from . import views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.Home, name='base'),
    path('Homw/', views.Home, name='base'),
   
]

# urlpatterns += staticfiles_urlpatterns()
