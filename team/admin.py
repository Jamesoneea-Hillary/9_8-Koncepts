from django.contrib import admin
from django.utils.html import format_html

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = (
        "preview_image",
        "full_name",
        "role",
        "is_featured",
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
        "is_featured",
        "role",
    )

    search_fields = (
        "full_name",
        "role",
        "short_bio",
        "bio",
        "email",
    )

    list_editable = (
        "is_featured",
        "is_active",
        "display_order",
    )

    ordering = (
        "display_order",
        "full_name",
    )

    readonly_fields = (
        "preview_image",
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "full_name",
                    "role",
                    "profile_image",
                    "preview_image",
                    "short_bio",
                    "bio",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                )
            },
        ),
        (
            "Social Profiles",
            {
                "fields": (
                    "linkedin_url",
                    "github_url",
                    "twitter_url",
                    "website_url",
                )
            },
        ),
        (
            "Website Display",
            {
                "fields": (
                    "is_active",
                    "is_featured",
                    "display_order",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    @admin.display(description="Photo")
    def preview_image(self, obj):

        if obj.profile_image:
            return format_html(
                '<img src="{}" width="60" height="60" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.profile_image.url
            )

        return "—"