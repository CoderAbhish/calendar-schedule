from django.urls import path

from . import views

# urlpatterns is a list of urls that represents the urls for this particular app.
urlpatterns = [
# path is a function that takes a url pattern and a view function as arguments and creates a url pattern for the app.
# the name argument is used to give a name to the url pattern so that we can use it in the templates and other places.
# <month> is a variable that we will use to capture the month from the url and pass it to the view function.
    path('<month>', views.monthly_challenge, name='month-challenge')
]