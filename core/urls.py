from django.conf import settings
from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
	path('home/', views.index, name='home'),
	path('contact/', views.contact, name='contact'),
	path('blog/', views.contact, name='blog'),
	path('pricing/', views.contact, name='pricing'),
	path('gallery/', views.contact, name='gallery'),
	path('about/', views.about, name='about'),
	path('services', views.services, name='services'),
	path('',views.index, name='')
]
