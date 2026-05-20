# calendar-schedule
This project is added to track the learning process for Django

## Module 1 - Routes and Views
### Commit 1 - First View and Route setup
#### 1.  Create Project *`django-admin startproject monthlySchedule`*
#### 2.  Create App/Module: *`django-admin startapp challenges`*
#### 3. Run server: *`python manage.py runserver`*
#### 4. Add View: ***challenges/views.py***
```python
from django.shortcuts import render
from django.http import HttpResponse

def january_index(request):
    return HttpResponse('January challenges are here')

def february_index(request):
    return HttpResponse('February challenges are here')
```
#### 5. Add App Specific Route: Add file ***challenges/url.py***
```python
    urlpatterns = [
        path('january', views.january_index),
        path('february', views.february_index)
    ]
```
#### 6. Register the Specific Route to the Project primary routing (URLconf): ***monthlySchedule/urls.py***
```python
    urlpatterns = [
        ...
        path('challenges/', include('challenges.url')),
    ]
```

### Commit 2 - Dynamic Path Segments and Captured Values
#### 1. Use Route parameter to make the URL dynamic: ***challenges/url.py***
```python
urlpatterns = [
    path('<month>', views.monthly_challenge)
]
```
#### 2. Handle the dynamic routing to change view content accordingly: ***challenges/views.py***
```python
monthlyChallenges = {
    'january': 'This is the January month Challenge',
    'february': 'This is the February month Challenge',
    'march': 'This is the March month Challenge',
    'april': 'This is the April month Challenge',
    'may': 'This is the May month Challenge',
    'june': 'This is the June month Challenge'
}

def monthly_challenge(request, month):
    if month in monthlyChallenges:
        return HttpResponse(monthlyChallenges[month])
    else:
        return HttpResponseNotFound('This month is not supported')
```

### Commit 3 - Path Converters
#### 1. Use path converters (https://docs.djangoproject.com/en/6.0/topics/http/urls/#path-converters) to route to specific View methods based on Route parameter data type:  ***challenges/url.py***
```python
urlpatterns = [
    path('<int:month>', views.monthly_challenge_by_number, name='int-month-challenge'),
    path('<str:month>', views.monthly_challenge, name='month-challenge')
]
```
#### 2. Modify the View methods accordingly: ***challenges/views.py***
```python
def monthly_challenge_by_number(request, month):
    months = (list)(monthlyChallenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This month is not supported')
    else:
        month_name = months[month - 1]
        return HttpResponse(monthlyChallenges[month_name])
```

### Commit 4 - Reverse and Route Redirection
#### 1. Reverse: https://docs.djangoproject.com/en/6.0/topics/http/urls/#reverse-resolution-of-urls 
```python
#challenges/views.py
redirect_path = reverse('month-challenge', args=[month_name]

#challenges/url.py
path('<str:month>', views.monthly_challenge, name='month-challenge')
```
#### 2. Redirection: https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/#redirect
```python
#challenges/views.py
return HttpResponseRedirect(redirect_path)
```

### Commit 5 - Returning HTML
#### 1. Returning HTML as response: https://docs.djangoproject.com/en/6.0/topics/http/views/#returning-an-httpresponse-object
```python
#challenges/views.py
def index(request):
    months = list(monthlyChallenges.keys())
    template_inner = ''
    for month in months:
        hyperlink = reverse('month-challenge', args=[month])
        template_inner += f'<li><a href="{hyperlink}"><h3>{month}</h3></a></li>\n'
    template = f'<ul>{template_inner}</ul>'
    return HttpResponse(template)

#challenges/url.py
urlpatterns = [
    # the actual route is /challenges/
    path('', views.index),
    ...
]
```

## Module 2 - Working with Templates and Static files
### Commit 1 - Adding and Registering Templates
#### 1. Adding HTML file to subfolder (create the subfolder). Path: **\<app\>/templates/<dir_appNamed>** e.g. -> *challenges/templates/challenges*
#### 2. Create **challenges.html** and **default.html** within the subfolder and populate it with your html code
```html
<!-- challenges/templates/challenges.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monthly Challenges</title>
</head>
<body>
    <h2>
        Let's assume this is the challenges page. We will be displaying all the challenges here.
    </h2>
</body>
</html>

<!-- challenges/templates/default.html -->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2 style="color: red;">
        Incorrect Month or Challenges for this month has not been added yet. Please check back later.
    </h2>
</body>
</html>

```
#### 3. Render these HTML pages on view - https://docs.djangoproject.com/en/6.0/topics/templates/#django.template.loader.render_to_string
```python
# challenges/views.py
...
from django.template.loader import render_to_string

...
def monthly_challenge(request, month):
    if month in monthlyChallenges:
        # render_to_string function is used to render the template and return the rendered template as a string
        _template = render_to_string('challenges/challenges.html')
        return HttpResponse(_template)
    else:
        _template = render_to_string('challenges/default.html')
        return HttpResponseNotFound(_template)
    
def monthly_challenge_by_number(request, month):
    months = (list)(monthlyChallenges.keys())
    if month > len(months):
        _template = render_to_string('challenges/default.html')
        return HttpResponseNotFound(_template)
    else:
        month_name = months[month - 1]
        redirect_path = reverse('month-challenge', args=[month_name]) 
        return HttpResponseRedirect(redirect_path)

```
#### 4. This still won't render because the loader is not able to find the template since we have not specified the path of the template in the settings.py file. We can make this work by following two methods:
**Option 1:** Load the template path within a list of Keys **TEMPLATES (Key -> 'DIRS')** in **settings.py**
```python
# monthlySchedule/settings.py
TEMPLATES = [
    {
        ...
        # we are telling django to look for the templates in the challenges/templates folder
        # dirs is a list of directories where django will look for the templates
        'DIRS': [
            BASE_DIR / 'challenges/templates'
        ],
        ...
    },
]
```
**Option 2:** Register the app **challenges** within the list **INSTALLED_APPS** in **settings.py**
```python
# monthlySchedule/settings.py

# Installed apps is a list of all the apps that are installed in our project and we want to use in our project
INSTALLED_APPS = [
    'challenges',
    ...
]

TEMPLATES = [
    {
        ...
        # we are telling django to look for the templates in the app folders as well
        # app_dirs is a boolean value that tells django to look for the templates in the app folders as well
        'APP_DIRS': True,
        ...
    },
]
```