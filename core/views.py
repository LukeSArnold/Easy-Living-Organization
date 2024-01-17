from django.shortcuts import render
from core.models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed
from core.forms import *
from django.shortcuts import get_object_or_404, render, redirect

class GeneralView:
    def index(request):
        return render(request, 'core/public/index.html')

    def pricing(request):
        return render(request, 'core/public/pricing.html')

    def gallery(request):
        return render(request, 'core/public/gallery.html')

    def blog(request):
        return render(request, 'core/public/blog.html')
    def contact(request):
        return render(request, 'core/public/contact.html')

    def about(request):
        return render(request, 'core/public/about.html')

    def services(request):
        return render(request, 'core/public/services.html')

class ManagerView:
    def home(request):
        return render(request, 'core/manager/manager_home.html')

    def metrics(request):
        return render(request, 'core/manager/metrics.html')

    def blog(request):
        return render(request, 'core/manager/manage_blog.html')

    def blog_entry(request):
        if request.method == "POST":
            form = BlogEntryForm(request.POST, request.FILES)
            if form.is_valid():
                # push information to the model
                # handle the stuff
                cover = form.cleaned_data.get('cover')
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                entry = Blog(title=title, content=content, cover=cover)
                entry.save()

                return redirect('manager/blog')
        return render(request, 'core/manager/manage_blog_entry.html')

    def gallery(request):
        return render(request, 'core/manager/manage_gallery.html')