from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView,DetailView

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')