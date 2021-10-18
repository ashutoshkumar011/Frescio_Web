from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path( '/sell', views.sellcrops , name='sell_crops' ),
    
]
