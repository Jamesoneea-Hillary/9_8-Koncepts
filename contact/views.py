from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactInquiryForm


def contact_view(request):

    if request.method == "POST":

        form = ContactInquiryForm(
            request.POST
        )

        if form.is_valid():

            inquiry = form.save()

            messages.success(
                request,
                (
                    "Thank you for reaching out! "
                    "Your inquiry has been received. "
                    "Our team will get back to you soon."
                )
            )

            return redirect(
                "contact:contact"
            )

    else:

        form = ContactInquiryForm()


    context = {
        "form": form,
    }


    return render(
        request,
        "contact/contact.html",
        context
    )