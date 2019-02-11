from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(HSC, PPC, Bidopt)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )
