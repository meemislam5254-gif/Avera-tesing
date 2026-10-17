from django.db import models
from django.conf import settings


class Foundation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='foundations/logos/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ChildWishlist(models.Model):
    child_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)  # e.g., "Winter Clothes & School Books"
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='wishlists/images/', blank=True, null=True)
    is_fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.child_name} - {self.title}"


class DonationTransaction(models.Model):
    DONATION_TYPES = (
        ('FOUNDATION', 'Verified Foundation'),
        ('WISHLIST', 'Child Wishlist'),
        ('DIRECT_FUND', 'AVERA Direct Fund'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
    )

    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES)

    # Target relations based on donation type
    foundation = models.ForeignKey(Foundation, on_delete=models.SET_NULL, null=True, blank=True)
    wishlist = models.ForeignKey(ChildWishlist, on_delete=models.SET_NULL, null=True, blank=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Payment Gateway Fields (SSLCommerz / bKash integration support)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation {self.transaction_id} - {self.amount} BDT ({self.donation_type})"


class DonorFeedback(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.donor.username} at {self.created_at.strftime('%Y-%m-%d')}"