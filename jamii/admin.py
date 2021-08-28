from django.contrib import admin
from .models import *

admin.site.site_header = "Jamii"


# Register your models here.
class ExporterAdmin(admin.ModelAdmin):
    list_display = 'Export_From', 'Export_To', 'Export_Industry'
    list_filter = ['Export_From', 'Export_Industry']


admin.site.register(Post)
admin.site.register(Exporter, ExporterAdmin)
admin.site.register(Glossary)
admin.site.register(Event)

