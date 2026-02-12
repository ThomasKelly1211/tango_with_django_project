from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! Here is the hyperlink to the about page --> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. go back to index page --> <a href='/rango/'>Index</a>")


