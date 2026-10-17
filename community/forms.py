from django import forms
from .models import MissingPersonReport

class MissingPersonReportForm(forms.ModelForm):
    class Meta:
        model = MissingPersonReport
        fields = ['person_type', 'name', 'age', 'gender', 'photo', 'last_seen_location', 'description', 'contact_number']