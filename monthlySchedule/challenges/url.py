from django.urls import path

from . import views

urlpatterns = [
    # says - if the url is an integer then call the monthly_challenge_by_number function and pass the month as an argument
    # all the data types used are defined in the django documentation - https://docs.djangoproject.com/en/6.0/topics/http/urls/#path-converters
    path('<int:month>', views.monthly_challenge_by_number),
    # name represents the name of the url pattern and/or the view function - it is used to reverse the url in the views.py file
    path('<str:month>', views.monthly_challenge, name='month-challenge')
]