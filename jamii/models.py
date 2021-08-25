from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    body = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(null=True, upload_to='images/')


class Exporter(models.Model):
    name = models.CharField(max_length=255)
    gdp = models.IntegerField()
    edb = models.IntegerField()  # EaseOfDoingBusiness

    def __str__(self):
        return self.name


class Importer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubIndustry(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255)
    exporter = models.ForeignKey(Exporter, on_delete=models.CASCADE)
    importer = models.ForeignKey(Importer, on_delete=models.CASCADE)
    sub_industry = models.ForeignKey(SubIndustry, on_delete=models.CASCADE)
    value = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.name

