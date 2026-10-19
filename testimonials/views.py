from django.shortcuts import render

from .models import Testimonial


def testimonial_list(request):

    testimonials = Testimonial.objects.filter(
        status="published"
    )

    context = {
        "testimonials": testimonials
    }

    return render(
        request,
        "testimonials/testimonial_list.html",
        context
    )