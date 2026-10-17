from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ChildAdoptionProfile, AdoptionApplication, AdopterProfile
from .forms import AdopterProfileForm, AdoptionApplicationForm, ChildAdoptionProfileForm


def adoption_home_view(request):
    children = ChildAdoptionProfile.objects.filter(is_adopted=False)
    return render(request, 'adoption/adoption_home.html', {'children': children})


@login_required
def create_adopter_profile_view(request):
    profile, created = AdopterProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AdopterProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Adopter Profile updated successfully!")
            return redirect('adoption_home')
    else:
        form = AdopterProfileForm(instance=profile)
    return render(request, 'adoption/adopter_profile.html', {'form': form})


@login_required
def apply_adoption_view(request, child_id):
    child = get_object_or_404(ChildAdoptionProfile, id=child_id)

    # Check if user has an adopter profile
    try:
        adopter_profile = request.user.adopter_profile
    except AdopterProfile.DoesNotExist:
        messages.warning(request, "Please complete your Adopter Profile before applying for adoption.")
        return redirect('create_adopter_profile')

    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.adopter = adopter_profile
            application.child = child
            application.save()
            messages.success(request, f"Adoption application submitted for {child.name}!")
            return redirect('adoption_home')
    else:
        form = AdoptionApplicationForm()

    return render(request, 'adoption/apply_adoption.html', {'form': form, 'child': child})