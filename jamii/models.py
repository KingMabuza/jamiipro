from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    description = models.CharField(max_length=255)
    body = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Importer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Exporter(models.Model):
    name = models.CharField(max_length=255)
    gdp = models.DecimalField(max_digits=19, decimal_places=2)
    edb = models.IntegerField()  # EaseOfDoingBusiness
    value = models.DecimalField(max_digits=19, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Glossary(models.Model):
    name = models.CharField(max_length=255)
    meaning = models.TextField(null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=255)
    body = RichTextField()

    def __str__(self):
        return self.name
