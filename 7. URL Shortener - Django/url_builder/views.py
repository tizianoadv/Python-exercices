from nis import match
from django.shortcuts import redirect
from django.shortcuts import render

from url_builder.models import TinyURL
from .forms import URLForm
import random
import string

def index(request):
    i=0

    context = {}

    # Get all URLs stored in database
    querySet = TinyURL.objects.order_by('-numberAccess').values()
    listURL = list(querySet.values('url'))
    listCode = list(querySet.values('shortcutCode'))
    listAccess = list(querySet.values('numberAccess'))

    # URlsto context(=dict)
    i=0
    while i < len(listURL) and i < 5:
        key = "url" + str(i)
        context[key] = listURL[i]['url']
        i+=1

    # Codes to context(=dict)
    i=0
    while i < len(listCode) and i < 5:
        key = "new_url" + str(i)
        context[key] = "http://shtURL/" + listCode[i]['shortcutCode']
        i+=1

    # Accesses to context(=dict)
    i=0
    while i < len(listAccess) and i < 5:
        key = "access" + str(i)
        context[key] = listAccess[i]['numberAccess']
        i+=1

    return render(request, 'url_builder/index.html', context)

def urlForm(request):
    
    sendAllow = False
    form = URLForm(None)
    context = {'form':form}

    if request.method == 'POST':
        form = URLForm(request.POST)
    
        if form.is_valid():
            sendAllow = True

    return render(request, 'url_builder/urlForm.html', context)

def redirection(request):
    nb_character = 5
    listURL = []
    i=0

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():

            # Catch POST data
            usernameForm = form.cleaned_data['username']
            urlForm = form.cleaned_data['url']

            # Get all URLs stored in database
            querySet = TinyURL.objects.all().values()
            l = list(querySet.values('url'))

            # Store URLs in list 
            while i < len(l):
                listURL.append(l[i]['url'])
                i+=1
            
            # Is URL already in Database ?
            if urlForm in listURL:
                print("in list")
                #Increase index
                matchURL = TinyURL.objects.get(url=urlForm)
                matchURL.numberAccess += 1
                matchURL.save()

            else:

                # Generate a new URL
                characters = string.ascii_letters + string.digits
                randomCode = [random.choice(characters) for _ in range(nb_character)]

                #Store new URL in database
                newURL = TinyURL(url=urlForm, shortcutCode=''.join(randomCode), username=usernameForm)
                newURL.save()
           
            return redirect('index')

        else:

            return redirect('urlForm')
    



