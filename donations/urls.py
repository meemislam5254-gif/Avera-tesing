from django.urls import path
from .views import donation_home_view, make_donation_view, donor_feedback_view

urlpatterns = [
    path('', donation_home_view, name='donation_home'),
    path('donate/<str:donation_type>/', make_donation_view, name='make_donation_direct'),
    path('donate/<str:donation_type>/<int:target_id>/', make_donation_view, name='make_donation_target'),
    path('feedback/', donor_feedback_view, name='donor_feedback'),
]