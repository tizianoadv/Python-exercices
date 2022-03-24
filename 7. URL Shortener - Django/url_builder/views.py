from django.shortcuts import redirect
from django.shortcuts import render
from .forms import URLForm

def index(request):
    return render(request, 'url_builder/index.html')

def urlForm(request):
    
    sendAllow = False
    form = URLForm(None)
    context = {'form':form}

    if request.method == 'POST':
        form = URLForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            url = form.cleaned_data['url']
            sendAllow = True

    return render(request, 'url_builder/urlForm.html', context)

def redirection(request):

    return redirect('index')
