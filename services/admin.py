from django.contrib import admin

from .models import (
    Service,
    ServiceFeature,
    ServiceTechnology,
    ServiceBenefit
)


class ServiceFeatureInline(admin.TabularInline):

    model = ServiceFeature

    extra = 1


class ServiceTechnologyInline(admin.TabularInline):

    model = ServiceTechnology

    extra = 1


class ServiceBenefitInline(admin.TabularInline):

    model = ServiceBenefit

    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "status",
        "is_featured",
        "order",
        "updated_at",
    )

    list_filter = (
        "status",
        "is_featured",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

    list_editable = (
        "status",
        "is_featured",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        ServiceFeatureInline,
        ServiceTechnologyInline,
        ServiceBenefitInline,
    ]

    fieldsets = (

        (
            "Service Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "icon",
                )
            }
        ),

        (
            "Service Content",
            {
                "fields": (
                    "short_description",
                    "description",
                    "hero_image",
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