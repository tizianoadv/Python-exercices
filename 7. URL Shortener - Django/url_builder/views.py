from django.shortcuts import render

def index(request):
    return render(request, 'url_builder/index.html')

def urlForm(request):
    return render(request, 'url_builder/urlForm.html')
