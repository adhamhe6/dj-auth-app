from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, PostForm
from django.contrib.auth import login
from .models import Post

def home(request):
    
    return render(request, 'main/home.html')


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('home'))
    else:
        form = PostForm()
        
    return render(request, "main/create_post.html", {'form':form})

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