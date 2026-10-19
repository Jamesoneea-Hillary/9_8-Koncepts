from django.contrib import admin

from .models import JobApplication, JobOpening


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "department",
        "employment_type",
        "work_mode",
        "is_featured",
        "is_active",
        "application_deadline",
        "created_at",
    )

    list_filter = (
        "is_active",
        "is_featured",
        "employment_type",
        "work_mode",
        "department",
    )

    search_fields = (
        "title",
        "department",
        "location",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "is_featured",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Position",
            {
                "fields": (
                    "title",
                    "slug",
                    "department",
                    "employment_type",
                    "work_mode",
                    "location",
                )
            },
        ),

        (
            "Job Description",
            {
                "fields": (
                    "short_description",
                    "description",
                    "responsibilities",
                    "requirements",
                    "nice_to_have",
                )
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "application_deadline",
                    "is_featured",
                    "is_active",
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


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "job",
        "email",
        "phone",
        "created_at",
    )

    list_filter = (
        "job",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "job__title",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Applicant",
            {
                "fields": (
                    "job",
                    "full_name",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Application",
            {
                "fields": (
                    "cover_letter",
                    "resume",
                    "portfolio_url",
                    "linkedin_url",
                    "github_url",
                )
            },
        ),

        (
            "Submitted",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )