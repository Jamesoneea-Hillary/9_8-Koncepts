from django.db import models


class Testimonial(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    RATING_CHOICES = [
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    ]

    client_name = models.CharField(
        max_length=150
    )

    client_position = models.CharField(
        max_length=150,
        blank=True,
        help_text="Example: CEO, Founder, Manager"
    )

    company_name = models.CharField(
        max_length=150,
        blank=True
    )

    client_photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    testimonial = models.TextField()

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    project_name = models.CharField(
        max_length=150,
        blank=True
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

        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):

        if self.company_name:
            return f"{self.client_name} - {self.company_name}"

        return self.client_name

    @property
    def initials(self):
        name_parts = self.client_name.split()
        if not name_parts:
            return "?"
        initials = name_parts[0][0]
        if len(name_parts) > 1:
            initials += name_parts[-1][0]
        return initials.upper()
