from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib import messages
from .models import *

# Create your views here.

def register(request):

    context = {}
    # if request.user.is_authenticated:
    #     return redirect('account')
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone')
            raw_pass = form.cleaned_data.get('password1')
            new_account = authenticate(phone=phone, password=raw_pass)
            login(request, new_account)
            return redirect('')
        else:
            context['signup_form'] = form
    else:
        form = SignupForm()
        context['signup_form'] = form
    return render(request, 'user/register.html', context)


