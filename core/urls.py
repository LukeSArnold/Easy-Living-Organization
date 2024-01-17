from django.conf import settings
from django.urls import path, include
from . import views

app_name = ''
urlpatterns = [
	path('home/', views.GeneralView.index, name='home'),
	path('contact/', views.GeneralView.contact, name='contact'),
	path('blog/', views.GeneralView.blog, name='blog'),
	path('pricing/', views.GeneralView.pricing, name='pricing'),
	path('gallery/', views.GeneralView.gallery, name='gallery'),
	path('about/', views.GeneralView.about, name='about'),
	path('services', views.GeneralView.services, name='services'),
	path('',views.GeneralView.index, name=''),
	path('manager/home', views.ManagerView.home, name='manager/home'),
	path('manager/gallery', views.ManagerView.gallery, name='manager/gallery'),
	path('manager/blog', views.ManagerView.blog, name='manager/blog'),
	path('manager/blog/entry', views.ManagerView.blog_entry, name='manager/blog/entry'),
	path('manager/metrics', views.ManagerView.metrics, name='manager/metrics'),
]
