from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserProfile

# Create your models here.


class Tags(models.Model):

    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class Category(models.Model):

    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)


class Articles(models.Model):

    title = models.CharField(max_length=255)
    desc = models.TextField()
    cover = models.CharField(max_length=255, null=True, blank=True)
    views = models.IntegerField(default=0)
    body = RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tags')
