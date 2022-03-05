#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect

# Create your views here.

def welcome(request):
    
    text = """<h1>Welcome to formula 1 blog</h1>"""

    return HttpResponse(text)

#Add argument in the GET resquest
def article(request, id_article):
    if int(id_article) > 100:
        raise Http404

    text = "<h1>You asked the article n° {}</h1>".format(id_article)

    return HttpResponse(text)

#Redirect a web page
def list_articles(request, year, month):
    return redirect("http://google.com")

#To redirect to another view
def redir(request):
    return redirect(redirview)

#View which is redirected
def redirview(request):
    text = "<h1>You have been redirected</h1>"
    return HttpResponse(text)