#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Hello world. I am Home. ")
    return render(request, "home.html")

def aboutpage(request):
    #return HttpResponse("Hello world. I am at about page")
    return render(request, "about.html")



