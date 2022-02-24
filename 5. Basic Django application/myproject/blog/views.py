from django.shortcuts import render

# Create your views here.

def helloWorld(request):

    age_jeff = 26
    weight_jeff = 70
    context = {'age' : age_jeff, 'weight' : weight_jeff}

    return render(request, 'index.html', context);