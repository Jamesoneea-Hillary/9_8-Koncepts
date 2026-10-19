from django.shortcuts import (
    get_object_or_404,
    render
)

from .models import Service


def service_list(request):

    services = Service.objects.filter(
        status="published"
    )

    context = {

        "services": services

    }

    return render(
        request,
        "services/service_list.html",
        context
    )


def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug,
        status="published"
    )

    context = {

        "service": service

    }

    return render(
        request,
        "services/service_detail.html",
        context
    )