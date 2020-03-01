from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def new(request):
    return render(request,'new.html')
def choose(request):
    return render(request,'choose.html')
def choosereg(request):
    return render(request,'choosereg.html')