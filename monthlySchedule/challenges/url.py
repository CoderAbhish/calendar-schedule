from django.urls import path

from . import views

# urlpatterns is a list of urls that represents the urls for this particular app.
urlpatterns = [
    path('january/', views.january_index),
    path('february/', views.february_index)
]