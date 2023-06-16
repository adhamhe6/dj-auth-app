from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import login

def home(request):
    
    return render(request, 'main/home.html')


def create_post(request):
        
    return render(request, "main/create_post.html")

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form':form})