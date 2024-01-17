from core.models import *
from django import forms

class BlogEntryForm(forms.Form):
    title = forms.CharField(max_length=255)
    cover = forms.ImageField()
    content = forms.CharField(widget=forms.Textarea)