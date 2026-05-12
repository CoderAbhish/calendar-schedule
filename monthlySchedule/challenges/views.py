from django.shortcuts import render
from django.http import HttpResponse

def january_index(request):
# HttpResponse is a class that represents the response that we will send back to the user. 
# It takes a string or html as an argument and sends it back to the user.
    return HttpResponse("This is the January Challenge")

def february_index(request):
    return HttpResponse("This is the February Challenge")