from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MissingPersonReport
from .forms import MissingPersonReportForm


def missing_reports_list_view(request):
    # শুধু যে রিপোর্টগুলো সমাধান (resolved) হয়নি সেগুলো দেখাবে
    reports = MissingPersonReport.objects.filter(is_resolved=False).order_by('-created_at')
    return render(request, 'community/missing_list.html', {'reports': reports})


@login_required
def report_missing_person_view(request):
    if request.method == 'POST':
        form = MissingPersonReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.save()
            messages.success(request, "Missing person report submitted successfully!")
            return redirect('missing_list')
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        form = MissingPersonReportForm()

    return render(request, 'community/report_missing.html', {'form': form})