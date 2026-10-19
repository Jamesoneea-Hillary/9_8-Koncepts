from django.db import models
from django.urls import reverse


class TeamMember(models.Model):
    full_name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)

    profile_image = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True
    )

    short_bio = models.TextField(
        max_length=300,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    # Social links
    linkedin_url = models.URLField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    twitter_url = models.URLField(
        blank=True
    )

    website_url = models.URLField(
        blank=True
    )

    # Display controls
    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "full_name"]
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.full_name} — {self.role}"

    def get_absolute_url(self):
        return reverse(
            "team:member_detail",
            kwargs={"pk": self.pk}
        )