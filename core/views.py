from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    return render(request, 'core/index.html')
# Create your views here.
