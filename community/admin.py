from django.contrib import admin
from .models import MissingPersonReport

@admin.register(MissingPersonReport)
class MissingPersonReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'person_type', 'last_seen_location', 'is_resolved', 'created_at')
    list_filter = ('person_type', 'is_resolved', 'created_at')
    search_fields = ('name', 'last_seen_location', 'description', 'contact_number')