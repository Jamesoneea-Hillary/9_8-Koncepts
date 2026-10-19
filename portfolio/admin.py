from django.contrib import admin

from .models import (
    ProjectCategory,
    Technology,
    Project,
    ProjectImage
)


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug"
    )

    prepopulated_fields = {
        "slug": (
            "name",
        )
    }


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "icon"
    )

    search_fields = (
        "name",
    )


class ProjectImageInline(
    admin.TabularInline
):

    model = ProjectImage

    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "client",
        "status",
        "is_featured",
        "display_order"
    )

    list_filter = (
        "category",
        "status",
        "is_featured"
    )

    search_fields = (
        "title",
        "client",
        "short_description"
    )

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

    filter_horizontal = (
        "technologies",
    )

    inlines = [
        ProjectImageInline
    ]