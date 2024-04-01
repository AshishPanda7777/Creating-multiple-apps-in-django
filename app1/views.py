from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    return HttpResponse('App1 is created')
