from django.shortcuts import render
from django.http import HttpResponse

def include():
    pass

def index(request):
    return HttpResponse("<b>Hello, world.</b> You're at the polls index.")

# Create your views here.
