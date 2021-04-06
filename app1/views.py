from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>welcome to index page1</h1>")

def hello(request):
    return render(request,"app1.html")

def sample_app1(request):
    return render(request,"sample_app1.html")



# Create your views here.
