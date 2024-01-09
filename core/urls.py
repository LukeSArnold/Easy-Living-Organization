from django.conf import settings
from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
	path('home/', views.index, name='home'),
]
