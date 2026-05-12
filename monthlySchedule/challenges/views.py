from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    
def monthly_challenge_by_number(request, month):
    months = (list)(monthlyChallenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This month is not supported')
    else:
        month_name = months[month - 1]
        #reverse function is used to get the url of the view function by passing the name of the view function and the arguments required by the view function
        redirect_path = reverse('month-challenge', args=[month_name]) #/challenges/march
        # Redirecting To the url with better format - instead of showing the url with the month number we will show the url with the month name
        return HttpResponseRedirect(redirect_path)