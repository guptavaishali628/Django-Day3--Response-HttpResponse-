from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(req):
    print("My first django project...")
    return HttpResponse("<h1 style='color:red;'>Welcome</h1>")
