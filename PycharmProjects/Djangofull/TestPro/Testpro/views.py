from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse("<h1>Tis is our Home page</h1>")

def News(request):
    return HttpResponse("<h1>This is our latest news</h1>")

def Contact(request):
    return HttpResponse("<h1>This is our contact us page</h1>")