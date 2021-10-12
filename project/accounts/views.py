from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success (request, f'Account created for {first_name}!')
            return redirect('')

    else:
        form = UserRegisterForm()

    return render (request, 'accounts/register.html', {'form': form})