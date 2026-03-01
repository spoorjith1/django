from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('Login')
    registerForm = UserCreationForm()
    context = {
        'registerForm' : registerForm
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            user = loginForm.get_user()
            auth.login(request, user)
            return redirect('Home')
    else:
        loginForm = AuthenticationForm()
    context = {
        'loginForm' : loginForm
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('Home')