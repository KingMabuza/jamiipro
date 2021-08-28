from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Exporter(models.Model):
    Type_of_Export = (
        ('Manufacturing', 'Manufacturing'),
        ('Textile', 'Textile'),
        ('Live Animals', 'Live Animals')
    )
    List_of_Country = (
        ('South Africa', 'South Africa'),
        ('Angola', 'Angola'),
        ('Botswana', 'Botswana'),
        ('Eswatini', 'Eswatini'),
        ('Mozambique', 'Mozambique')
    )
    Export_Industry = models.TextField(max_length=500, choices=Type_of_Export, blank=True)
    Export_From = models.TextField(max_length=500, choices=List_of_Country, blank=True)
    Export_To = models.TextField(max_length=500, choices=List_of_Country, blank=True)
    Export_Prohibitions = RichTextField(null=True)
    Export_Sanitary_Phytosanitary_Measures = RichTextField(null=True)
    Export_Taxes = RichTextField(null=True)
    Export_License = RichTextField(null=True)

    def __str__(self):
        return self.Export_Industry


class Glossary(models.Model):
    name = models.CharField(max_length=255)
    meaning = models.TextField(null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
    description = RichTextField(null=True)
    location = models.CharField(max_length=255)
    booking_url = models.URLField(null=True)
    event_cover = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.name
