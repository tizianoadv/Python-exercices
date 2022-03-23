from django.shortcuts import render

def index(request):
    return render(request, 'url_builder/index.html')

def builder(request):
    return render(request, 'url_builder/builder.html')
