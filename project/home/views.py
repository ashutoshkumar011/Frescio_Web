from django.http.response import HttpResponse, HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import csv
# Create your views here.

def home(request):
    return render( request, 'home/homepage.html' )
    # return render(request, 'home/base.html' )

def register(request):
    return render( request, 'home/register.html' )

def fertilizer(request):
    context = {}
    # context['crop'] = {'sdf','asd','lol'}
    data=[]
    # data = pd.read_csv("fertilizer.csv")
    with open('home/fertilizer.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row[1])
    data.sort()
    context['crop'] = data

    return render( request, 'home/fertilizer.html',context)

def fertpred(request):
    return render( request, 'home/fertilizer_result.html')