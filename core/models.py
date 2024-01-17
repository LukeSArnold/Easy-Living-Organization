from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    cover = models.ImageField()
    content = models.TextField()
    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Id = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    firstName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField()


class MailList(models.Model):
    lastName = models.CharField(max_length=100, blank=True, null=True)
    firstName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    promotional = models.BooleanField()


class Interactions(models.Model):
    pageViews = models.IntegerField()
    ctaClicks = models.IntegerField()
