from django.contrib import admin

from .models import (
    SiteSettings,
    CompanyStatistic,
    Technology,
    Partner,
    AssistantConversation,
    AssistantSubmission,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "email",
        "phone",
        "updated_at"
    )

    def has_add_permission(self, request):

        # Allow adding only when no settings exist
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):

        # Prevent accidental deletion
        return False


@admin.register(CompanyStatistic)
class CompanyStatisticAdmin(admin.ModelAdmin):

    list_display = (
        "number",
        "label",
        "order"
    )

    list_editable = (
        "order",
    )


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "is_featured",
        "order"
    )

    list_filter = (
        "is_featured",
        "category"
    )

    list_editable = (
        "order",
        "is_featured"
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "order"
    )

    list_editable = (
        "is_active",
        "order"
    )


@admin.register(AssistantConversation)
class AssistantConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at")
    readonly_fields = ("session_key", "messages", "created_at", "updated_at")
    search_fields = ("session_key",)
    ordering = ("-updated_at",)

    def has_add_permission(self, request):
        return False


@admin.register(AssistantSubmission)
class AssistantSubmissionAdmin(admin.ModelAdmin):
    list_display = ("token", "created_at")
    readonly_fields = ("token", "created_at")
    def has_add_permission(self, request):
        return False
