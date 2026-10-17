from django.db import models
from django.conf import settings

class MissingPersonReport(models.Model):
    PERSON_TYPE_CHOICES = (
        ('CHILD', 'Child'),
        ('ELDERLY', 'Elderly'),
        ('OTHER', 'Other'),
    )

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='missing_reports')
    person_type = models.CharField(max_length=20, choices=PERSON_TYPE_CHOICES, default='CHILD')
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')), blank=True, null=True)
    photo = models.ImageField(upload_to='missing_photos/', blank=True, null=True)
    last_seen_location = models.CharField(max_length=255)
    description = models.TextField()
    contact_number = models.CharField(max_length=20)
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Missing: {self.name or 'Unknown'} ({self.person_type})"