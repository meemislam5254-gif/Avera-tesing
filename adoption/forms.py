from django import forms
from .models import AdopterProfile, AdoptionApplication, ChildAdoptionProfile

class AdopterProfileForm(forms.ModelForm):
    class Meta:
        model = AdopterProfile
        fields = ['nid_number', 'occupation', 'monthly_income', 'address']

class ChildAdoptionProfileForm(forms.ModelForm):
    class Meta:
        model = ChildAdoptionProfile
        fields = ['name', 'age', 'gender', 'photo', 'health_details']

class AdoptionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdoptionApplication
        fields = ['application_reason']