from django.contrib import admin
from .models import AdopterProfile, ChildAdoptionProfile, AdoptionApplication

@admin.register(AdopterProfile)
class AdopterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nid_number', 'monthly_income', 'is_verified', 'created_at')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'nid_number')

@admin.register(ChildAdoptionProfile)
class ChildAdoptionProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'guardian', 'age', 'gender', 'is_adopted', 'created_at')
    list_filter = ('gender', 'is_adopted')
    search_fields = ('name', 'guardian__username')

@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('adopter', 'child', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('adopter__user__username', 'child__name')