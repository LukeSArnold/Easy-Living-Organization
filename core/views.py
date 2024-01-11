from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    return render(request, 'core/index.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

