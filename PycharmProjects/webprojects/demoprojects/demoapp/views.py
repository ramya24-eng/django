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
from newsapi import NewsApiClient
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    return render(request, 'demoapp/home.html')

def login(request):
    return render(request,'demoapp/login.html')

def profile_post(request):
    context1 = {'post', Post.objects.all()}
    return render(request,'demoapp/profile_post.html',{'context1':context1})

class PostListView(ListView):
    model= Post
    template_name = 'home.html'
    context_object_name = 'post'
    ordering = ['-date_published']

def createaccount(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form is not None:
            if form.is_valid():
               form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
            return render(request, 'demoapp/createaccount.html', {'form': form})
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
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_everything(
                                          domains='bbc.co.uk,techcrunch.com',
                                          language='en',
                                          sort_by='relevancy'  )

    articles = topheadlines['articles']
    desc = []
    news = []
    img = []
    link = []
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)


    return render(request,'demoapp/news.html', context={"mylist":mylist})

def business(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_top_headlines(category='business',
                                            language='en',
                                            country='in')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)

    return render(request,'demoapp/newscontent.html', context={"mylist":mylist})

def entertainment(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_top_headlines(category='entertainment',
                                            language='en',
                                            country='in')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)
    return render(request,'demoapp/newscontent.html', context={"mylist":mylist})

def technology(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_top_headlines(category='technology',
                                            language='en',
                                            country='in',page=3)

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)

    return render(request,'demoapp/newscontent.html', context={"mylist":mylist})

def sports(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_top_headlines(category='sports',
                                            language='en',
                                            country='in')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)

    return render(request,'demoapp/newscontent.html', context={"mylist":mylist})

def health(request):
    newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
    topheadlines = newsapi.get_top_headlines(category='health',
                                            language='en',
                                            country='in')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    link = []
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        link.append(myarticles['url'])

    mylist = zip(news, desc, img, link)

    return render(request,'demoapp/newscontent.html', context={"mylist":mylist})

def search(request):
    if request.method =="GET":
        count=0
        query = request.GET.get('Search')
        newsapi = NewsApiClient(api_key="eb543432c3bb4da8af5653c66ca2e805")
        topheadlines = newsapi.get_everything(q=query,
                                          language='en',
                                          sort_by='relevancy'
                                          )

        articles = topheadlines['articles']

        desc = []
        news = []
        img = []
        link = []
        for i in range(len(articles)):
            myarticles = articles[i]
            content=myarticles['description']
            print(content)
            if query in content:
                myarticles = articles[i]
                count+=1
                news.append(myarticles['title'])
                desc.append(myarticles['description'])
                img.append(myarticles['urlToImage'])
                link.append(myarticles['url'])
            else:
                continue
        mylist = zip(news, desc, img, link)

        if count == 0:
            return HttpResponse("Result Not Found")
        else:
            return render(request, 'demoapp/newscontent.html', context={"mylist": mylist})

