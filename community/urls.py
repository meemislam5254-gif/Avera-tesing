from django.urls import path
from .views import missing_reports_list_view, report_missing_person_view

urlpatterns = [
    path('', missing_reports_list_view, name='missing_list'),
    path('report/', report_missing_person_view, name='report_missing'),
]