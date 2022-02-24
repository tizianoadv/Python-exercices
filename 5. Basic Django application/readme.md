# A basic Django application

## Requirements

### Packages installation

> sudo apt update
>
> sudo apt -y upgrade 
>
> sudo apt-get -y install python3.8 python3.8-venv pip

### Create a virtual environment

> python3 -m venv venv

### Activate the virtual environment

> source venv/bin/activate

***To desactivate the virtual environement***

> deactivate

### Python Django package installation

> pip install django

### Start a new project

> django-admin startproject myproject

### Launch a server

> python3 manage.py runserver

### Browse to the server from your favorite browser

> 127.0.0.1:8000

## Create a blog

> python3 manage.py startapp blog

- It would be better set name starting with an upper case

- add the blog within myproject/myproject/settings.py

```Python
# Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog'
    ]
```
### Create a template

- Used to put HTML files

> mkdir -p myproject/blog/templates
>
> vi myproject/blog/templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>
```

### Create a view 

> vi myproject/blog/views.py

```Python
def helloWorld(request):
    return render(request, 'index.html');
```

### Create a personalised URL

> vi myproject/myproject/urls.py

```Python
from django.contrib import admin
from django.urls import path
from blog.views import helloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', helloWorld)
]
```

### Run the server

> python3 manage.py runserver

### Browse 

> http://127.0.0.1:8000/hello/

## Dynamic web page

### Modify views

> vi myproject/blog/views.py

```Python
def helloWorld(request):

    age_jeff = 26
    weight_jeff = 70
    context = {'age' : age_jeff, 'weight' : weight_jeff}

    return render(request, 'index.html', context);
```

### Modify index.html

> vi myproject/blog/templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h2>data:</h2>
    <p>Age: {{age}}</p>
    <p>Weight: {{weight}}</p>
</body>
</html>
```

### Browse 

> http://127.0.0.1:8000/hello/