# Blog with Django - commands history

## Requirements

### Packages installation

> sudo apt update
>
> sudo apt -y upgrade
>
> sudo apt-get -y install python3.8 python3.8-venv pip

### Python Django package installation

> pip install django

### Create a virtual environment

> python3 -m venv venv
>
> source venv/bin/activate

***To deactivate a virtual environment***

> deactivate

## Create a blog

> django-admin startproject formula1
> 
> cd formula1
>
> mkdir templates

### Configuration details

***Debug Mode***

```python
DEBUG = True
```

***Admin***

```python
ADMINS = [
    ('Firstname Lastname', 'email')
]
```

***Database***

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

***Time & language***

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'
```

***Templates paths***

By adding the following code to the DIRS argument, the templates folder 
created before at the same location as manage.py would be consider. Normally, all specific templates located within all 
applications would also be consider.

> os.path.join(BASE_DIR,'templates')

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

***Appending a slash in URL***

Add a slash at the end of URL if there is no slash

```python
APPEND_SLASH = True
```

## Create an application

> python3 manage.py startapp blog

### Update settings applications

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog' #Add the blog application
]
```
