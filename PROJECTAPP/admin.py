from django.contrib import admin
from .models import Code
# Register your models here.
from import_export.admin import ImportExportModelAdmin
#admin.site.register(Code)

@admin.register(Code)
class ViewAdmin(ImportExportModelAdmin):
    pass