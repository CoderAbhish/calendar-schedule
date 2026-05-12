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