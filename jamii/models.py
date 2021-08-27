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


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Importer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Exporter(models.Model):

    Type_of_Export = (
        ('Manufacturing', 'Manufacturing'),
        ('Textile', 'Textile'),
        )
    List_of_Country =  (
        ('RSA', 'RSA'),
        ('Angola', 'Angola'),
    ) 
    Export_Industry = models.TextField(max_length=500,choices=Type_of_Export, blank=True)
    Export_From = models.TextField(max_length=500,choices=List_of_Country, blank=True)
    Export_To = models.TextField(max_length=500,choices=List_of_Country, blank=True)
    Export_From_gdp = models.DecimalField(max_digits=19, decimal_places=2)
    Export_From_edb = models.IntegerField()  # EaseOfDoingBusiness

    def __str__(self):
        return self.Export_Industry

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

class Profile(models.Model):
    UserType = (
        ('Entrepreneur', 'Entrepreneur'),
        ('AFCFTA', 'AFCFTA'),
    )
    Origin = (
        ('RSA', 'RSA'),
        ('Angola', 'Angola'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Type_of_user = models.TextField(max_length=500,choices=UserType, blank=True)
    User_origin = models.TextField(max_length=500,choices=Origin, blank=True)
    # domain_of_Knowledge = models.CharField(max_length=500, choices=Domain, blank=True)
    # type_of_paper = models.CharField(max_length=500, choices=Paper, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


