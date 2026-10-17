from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import uuid
from .models import Foundation, ChildWishlist, DonationTransaction, DonorFeedback


def donation_home_view(request):
    foundations = Foundation.objects.filter(is_verified=True)
    wishlists = ChildWishlist.objects.filter(is_fulfilled=False)
    return render(request, 'donations/donation_home.html', {
        'foundations': foundations,
        'wishlists': wishlists,
    })


@login_required
def make_donation_view(request, donation_type, target_id=None):
    foundation = None
    wishlist = None

    # URL case handling
    type_upper = donation_type.upper() if donation_type else ''

    if type_upper == 'FOUNDATION' and target_id:
        foundation = get_object_or_404(Foundation, id=target_id)
    elif type_upper == 'WISHLIST' and target_id:
        wishlist = get_object_or_404(ChildWishlist, id=target_id)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount and float(amount) > 0:
            # Payment Transaction creation (Simulated Sandbox Flow)
            trx_id = f"AVERA-{uuid.uuid4().hex[:10].upper()}"

            transaction = DonationTransaction.objects.create(
                donor=request.user,
                donation_type=type_upper,
                foundation=foundation,
                wishlist=wishlist,
                amount=amount,
                transaction_id=trx_id,
                payment_status='COMPLETED'  # Mocking instant payment success
            )

            # Update wishlist raised amount if applicable
            if wishlist:
                wishlist.raised_amount += float(amount)
                if wishlist.raised_amount >= wishlist.target_amount:
                    wishlist.is_fulfilled = True
                wishlist.save()

            messages.success(request,
                             f"Thank you! Your donation of {amount} BDT was successful. Transaction ID: {trx_id}")
            return redirect('donation_home')
        else:
            messages.error(request, "Please enter a valid amount.")

    return render(request, 'donations/make_donation.html', {
        'donation_type': donation_type,
        'foundation': foundation,
        'wishlist': wishlist,
    })


@login_required
def donor_feedback_view(request):
    if request.method == 'POST':
        # Accept either 'message' or 'comment' from template form
        message = request.POST.get('message') or request.POST.get('comment')

        if message:
            DonorFeedback.objects.create(
                donor=request.user,
                message=message
            )
            messages.success(request, "Your feedback has been sent to AVERA Admin!")
            return redirect('donation_home')
        else:
            messages.error(request, "Please write a message before submitting.")

    return render(request, 'donations/feedback.html')