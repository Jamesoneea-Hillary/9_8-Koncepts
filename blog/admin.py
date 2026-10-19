from django.contrib import admin

from .models import (
    BlogPost,
    Category,
    NewsletterSubscriber,
    Tag,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "author",
        "published_at",
        "created_at",
    )

    list_filter = (
        "status",
        "is_featured",
        "category",
        "tags",
        "created_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = (
        "tags",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Article Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "content",
                    "featured_image",
                ),
            },
        ),
        (
            "Classification",
            {
                "fields": (
                    "category",
                    "tags",
                ),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "author",
                    "status",
                    "is_featured",
                    "published_at",
                ),
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):

    list_display = (
        "email",
        "is_active",
        "subscribed_at",
    )

    list_filter = (
        "is_active",
        "subscribed_at",
    )

    search_fields = (
        "email",
    )

    readonly_fields = (
        "subscribed_at",
    )
