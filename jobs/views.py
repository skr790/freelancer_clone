
from django.shortcuts import render
from django.http import HttpResponse,request

def index(request):
    return render(request,'jobs/index.html')

def about(request):
    return HttpResponse('<h1>Hello</h1>')