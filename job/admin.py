from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'company_name', 'requirements', 'salary']
    list_per_page = 20
    search_fields = ['title','company_name']