from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='homepage' ),
    # path('register', views.register, name='register')
    # path('register', views.register, name='register')
    # path('register', include('accounts.urls')),

]