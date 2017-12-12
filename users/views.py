from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
            form = RegisterForm()
    return render(request, 'users/register.html', context={'form': form})

def index(request):
    return render(request, 'index.html')


def user_login(request):
    redirect_to = request.POST.get('next', request.GET.get('next',''))

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', context={'form': form})