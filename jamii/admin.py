from django.contrib import admin
from .models import *

admin.site.site_header = "Jamii"
# Register your models here.
admin.site.register(Post)
admin.site.register(Exporter)
admin.site.register(Importer)
admin.site.register(Category)
admin.site.register(Glossary)
admin.site.register(About)
