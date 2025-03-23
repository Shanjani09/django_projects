from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def home(request):
    return HttpResponse("This is Home Page...!!")
def firstpage(request):
    return HttpResponse("Welcome to first Page..!!!")
def secondpage(request):
    return HttpResponse("Welcome to second page...!!!")
def htmlpg(request):
    return render(request,'template.html')