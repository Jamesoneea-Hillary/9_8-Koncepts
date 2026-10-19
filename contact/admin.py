from django.contrib import admin

from .models import ContactInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "service",
        "budget",
        "status",
        "is_read",
        "created_at",
        "source",
    )


    list_filter = (
        "service",
        "budget",
        "status",
        "is_read",
        "created_at",
        "source",
    )


    search_fields = (
        "full_name",
        "email",
        "company",
        "message",
    )


    readonly_fields = (
        "created_at",
        "updated_at",
    )


    ordering = (
        "-created_at",
    )


    fieldsets = (

        (
            "Client Information",
            {
                "fields": (
                    "full_name",
                    "email",
                    "phone",
                    "company",
                )
            }
        ),

        (
            "Project Information",
            {
                "fields": (
                    "service",
                    "budget",
                    "message",
                    "source",
                    "assistant_conversation",
                )
            }
        ),

        (
            "Inquiry Management",
            {
                "fields": (
                    "status",
                    "is_read",
                )
            }
        ),

        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )
