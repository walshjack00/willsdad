from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ExcelSheet)
class excelSheetAdmin(admin.ModelAdmin):
    model = models.ExcelSheet