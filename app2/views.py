from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>welcome to index page2</h1>")

def sample2(request):
    return render(request,"app2.html")

def sample_app2(request):
    return render(request,"sample_app2.html")


# Create your views here.
