# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'demoapp/home.html')

def profile_post(request):
    context1 = {'post', Post.objects.all()}
    return render(request,'demoapp/profile_post.html',context1)

class PostListView(ListView):
    model= Post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_published']

def createaccount(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        return render(request,'demoapp/createaccount.html',{'form':form})

@login_required
def profile(request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form=PostForm()
        return render(request,'demoapp/profile.html',{'form':form})

def news(request):
    return render(request,'demoapp/news.html')