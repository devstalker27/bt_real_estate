from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'title': 'Index'}
    return render(request, 'pages/index.html', context=context)


def about(request):
    title = 'About'
    items = ['1', '2', '3', '4']
    context = {'title': title, 'items': items}
    return render(request, 'pages/about.html', context=context)
