from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def letters(request):
    template = loader.get_template('letters.html')
    return HttpResponse(template.render())

def form(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())

def capsules(request):
    template = loader.get_template('capsules.html')
    return HttpResponse(template.render())

