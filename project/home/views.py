from django.http.response import HttpResponse, HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render( request, 'home/homepage.html' )
    # return render(request, 'home/base.html' )
