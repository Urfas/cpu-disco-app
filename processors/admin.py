from django.contrib import admin
from .models import Processor

@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'cores', 'threads', 'release_year', 'overall_score')
    list_filter = ('manufacturer', 'release_year', 'integrated_graphics')
    search_fields = ('name', 'series')
    list_per_page = 50
