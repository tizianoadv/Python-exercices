from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'url_builder/index.html')

def builder(request):
    return render(request, 'url_builder/builder.html')
