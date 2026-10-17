from django.urls import path
from .views import adoption_home_view, create_adopter_profile_view, apply_adoption_view

urlpatterns = [
    path('', adoption_home_view, name='adoption_home'),
    path('profile/', create_adopter_profile_view, name='create_adopter_profile'),
    path('apply/<int:child_id>/', apply_adoption_view, name='apply_adoption'),
]