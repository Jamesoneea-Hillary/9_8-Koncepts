from django.db import models
import uuid


class AssistantConversation(models.Model):
    """Short-lived, session-owned assistant transcript for context and review."""
    session_key = models.CharField(max_length=40, db_index=True)
    messages = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Assistant conversation {self.pk}"


class AssistantSubmission(models.Model):
    """Idempotency token for assistant leads; no duplicate lead store."""
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


class SiteSettings(models.Model):

    company_name = models.CharField(
        max_length=150,
        default="Nine Eight Koncepts"
    )

    tagline = models.CharField(
        max_length=255,
        blank=True
    )

    company_description = models.TextField(
        blank=True
    )

    logo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    favicon = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    map_embed_url = models.URLField(
        blank=True,
        help_text="Paste the Google Maps embed URL (the src URL from Share > Embed a map)."
    )

    whatsapp_number = models.CharField(
        max_length=30,
        blank=True
    )

    facebook_url = models.URLField(
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):

        # Ensure only one SiteSettings instance exists
        if not self.pk and SiteSettings.objects.exists():
            existing = SiteSettings.objects.first()
            self.pk = existing.pk

        super().save(*args, **kwargs)

    def __str__(self):
        return self.company_name

class CompanyStatistic(models.Model):

    number = models.CharField(
        max_length=20,
        help_text="Example: 50+"
    )

    label = models.CharField(
        max_length=100,
        help_text="Example: Projects Delivered"
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap icon class"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = ["order"]

        verbose_name = "Company Statistic"
        verbose_name_plural = "Company Statistics"

    def __str__(self):

        return f"{self.number} {self.label}"

class Technology(models.Model):

    name = models.CharField(
        max_length=100
    )

    logo = models.ImageField(
        upload_to="technologies/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_featured = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = ["order"]

        verbose_name = "Technology"
        verbose_name_plural = "Technologies"

    def __str__(self):

        return self.name

class Partner(models.Model):
    name = models.CharField(
        max_length=150
    )

    logo = models.ImageField(
        upload_to="partners/"
    )

    website = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:

        ordering = ["order"]

    def __str__(self):

        return self.name