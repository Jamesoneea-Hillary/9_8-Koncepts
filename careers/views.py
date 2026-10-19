from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobApplicationForm
from .models import JobOpening


def careers_list(request):

    jobs = (
        JobOpening.objects
        .filter(is_active=True)
        .order_by(
            "-is_featured",
            "-created_at"
        )
    )

    featured_jobs = jobs.filter(
        is_featured=True
    )

    context = {
        "jobs": jobs,
        "featured_jobs": featured_jobs,
    }

    return render(
        request,
        "careers/careers_list.html",
        context
    )


def job_detail(request, slug):

    job = get_object_or_404(
        JobOpening,
        slug=slug,
        is_active=True
    )

    form = JobApplicationForm()

    context = {
        "job": job,
        "form": form,
    }

    return render(
        request,
        "careers/partials/job_detail.html",
        context
    )


def apply_for_job(request, slug):

    job = get_object_or_404(
        JobOpening,
        slug=slug,
        is_active=True
    )

    if request.method != "POST":
        return redirect(job.get_absolute_url())

    form = JobApplicationForm(
        request.POST,
        request.FILES
    )

    if form.is_valid():

        application = form.save(
            commit=False
        )

        application.job = job

        application.save()

        messages.success(
            request,
            "Your application has been submitted successfully."
        )

        return redirect(
            "careers:application_success"
        )

    context = {
        "job": job,
        "form": form,
    }

    return render(
        request,
        "careers/partials/job_detail.html",
        context
    )


def application_success(request):

    return render(
        request,
        "careers/partials/application_success.html"
    )
