from django.db import models
from django.utils.text import slugify


class Service(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    title = models.CharField(
        max_length=150
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap Icon class. Example: bi-code-slash"
    )

    short_description = models.CharField(
        max_length=255
    )

    description = models.TextField()

    hero_image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "order",
            "-created_at"
        ]

        verbose_name = "Service"

        verbose_name_plural = "Services"

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                self.title
            )

        super().save(
            *args,
            **kwargs
        )


class ServiceFeature(models.Model):

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="features"
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        default="bi-check-circle-fill"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "order",
            "id"
        ]

        verbose_name = "Service Feature"

        verbose_name_plural = "Service Features"

    def __str__(self):

        return f"{self.service.title} - {self.title}"


class ServiceTechnology(models.Model):

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="technologies"
    )

    name = models.CharField(
        max_length=100
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional Bootstrap Icon class"
    )

    logo = models.ImageField(
        upload_to="services/technologies/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "order",
            "name"
        ]

        verbose_name = "Service Technology"

        verbose_name_plural = "Service Technologies"

    def __str__(self):

        return self.name


class ServiceBenefit(models.Model):

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="benefits"
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        default="bi-lightning-charge"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "order",
            "id"
        ]

        verbose_name = "Service Benefit"

        verbose_name_plural = "Service Benefits"

    def __str__(self):

        return f"{self.service.title} - {self.title}"