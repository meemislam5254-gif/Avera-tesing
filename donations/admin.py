from django.contrib import admin
from .models import Foundation, ChildWishlist, DonationTransaction, DonorFeedback

@admin.register(Foundation)
class FoundationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verified', 'created_at')
    list_filter = ('is_verified',)
    search_fields = ('name',)

@admin.register(ChildWishlist)
class ChildWishlistAdmin(admin.ModelAdmin):
    list_display = ('child_name', 'title', 'target_amount', 'raised_amount', 'is_fulfilled', 'created_at')
    list_filter = ('is_fulfilled',)
    search_fields = ('child_name', 'title')

@admin.register(DonationTransaction)
class DonationTransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'donor', 'donation_type', 'amount', 'payment_status', 'created_at')
    list_filter = ('donation_type', 'payment_status')
    search_fields = ('transaction_id', 'donor__username')

@admin.register(DonorFeedback)
class DonorFeedbackAdmin(admin.ModelAdmin):
    list_display = ('donor', 'message', 'created_at')
    search_fields = ('donor__username', 'message')