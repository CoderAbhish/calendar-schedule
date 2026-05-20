from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthlyChallenges = {
    'january': 'This is the January month Challenge',
    'february': 'This is the February month Challenge',
    'march': 'This is the March month Challenge',
    'april': 'This is the April month Challenge',
    'may': 'This is the May month Challenge',
    'june': 'This is the June month Challenge'
}

def index(request):
    months = list(monthlyChallenges.keys())
    template_inner = ''
    for month in months:
        hyperlink = reverse('month-challenge', args=[month])
        template_inner += f'<li><a href="{hyperlink}"><h3>{month}</h3></a></li>\n'
    template = f'<ul>{template_inner}</ul>'
    return HttpResponse(template)

def monthly_challenge(request, month):
    if month in monthlyChallenges:
        # _template = render_to_string('challenges/challenges.html', {
        #     'text': monthlyChallenges[month],
        #     'month_name': month
        # })
        # return HttpResponse(_template)

        # remember that render function is a shortcut function that combines the render_to_string and HttpResponse functions
        return render(request, 'challenges/challenges.html', {
            'text': monthlyChallenges[month],
            'month_name': month
        })
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
        #reverse function is used to get the url of the view function by passing the name of the view function and the arguments required by the view function
        redirect_path = reverse('month-challenge', args=[month_name]) #/challenges/march
        # Redirecting To the url with better format - instead of showing the url with the month number we will show the url with the month name
        return HttpResponseRedirect(redirect_path)