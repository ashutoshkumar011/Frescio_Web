from django.http.response import HttpResponse, HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')