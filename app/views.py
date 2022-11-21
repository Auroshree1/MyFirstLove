from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('My first project')
def message(request):
    return HttpResponse('Hello all')