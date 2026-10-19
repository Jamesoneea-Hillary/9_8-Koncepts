from django.contrib import admin
from django.utils.html import format_html

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "client_name",
        "client_avatar_preview",
        "company_name",
        "rating",
        "status",
        "is_featured",
        "order",
        "created_at",
    )

    list_filter = (
        "status",
        "rating",
        "is_featured",
    )

    search_fields = (
        "client_name",
        "company_name",
        "project_name",
        "testimonial",
    )

    list_editable = (
        "status",
        "is_featured",
        "order",
    )

    readonly_fields = (
        "client_avatar_preview",
        "created_at",
        "updated_at",
    )

    @admin.display(description="Avatar")
    def client_avatar_preview(self, obj):
        if not obj or not obj.client_photo:
            return "No photo uploaded"
        return format_html(
            '<img src="{}" alt="" style="width:40px;height:40px;object-fit:cover;border-radius:50%;" />',
            obj.client_photo.url,
        )

    fieldsets = (

        (
            "Client Information",
            {
                "fields": (
                    "client_name",
                    "client_position",
                    "company_name",
                    "client_photo",
                    "client_avatar_preview",
                )
            }
        ),

        (
            "Testimonial",
            {
                "fields": (
                    "testimonial",
                    "rating",
                    "project_name",
                )
            }
        ),

        (
            "Publishing",
            {
                "fields": (
                    "status",
                    "is_featured",
                    "order",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )
