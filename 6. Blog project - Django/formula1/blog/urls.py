from django.urls import path
from blog.views import *

urlpatterns = [
    path('welcome/', welcome),
    path('article/<int:id_article>',article), #Add argument or raise 404 error
    path('list/<int:year>/<int:month>', list_articles), #To redirect a webpage
    path('redir', redir), #To redirect to another view
    path('redirview', redirview) #View which is redirected
]