from django.db import models


class ContactInquiry(models.Model):

    SERVICE_CHOICES = [
        ("website", "Website Design & Development"),
        ("web_app", "Web Application Development"),
        ("mobile_app", "Mobile Application Development"),
        ("software", "Custom Software Development"),
        ("maintenance", "Website & Software Maintenance"),
        ("consultation", "Software Consultation"),
        ("other", "Other"),
    ]


    BUDGET_CHOICES = [
        ("below_1m", "Below UGX 1,000,000"),
        ("1m_3m", "UGX 1,000,000 - 3,000,000"),
        ("3m_5m", "UGX 3,000,000 - 5,000,000"),
        ("5m_10m", "UGX 5,000,000 - 10,000,000"),
        ("above_10m", "Above UGX 10,000,000"),
        ("not_sure", "Not Sure Yet"),
    ]


    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("archived", "Archived"),
    ]


    # CLIENT INFORMATION

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    company = models.CharField(
        max_length=150,
        blank=True
    )


    # PROJECT INFORMATION

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES
    )

    budget = models.CharField(
        max_length=50,
        choices=BUDGET_CHOICES,
        blank=True
    )

    message = models.TextField()

    source = models.CharField(max_length=30, default="website", db_index=True)
    assistant_conversation = models.ForeignKey(
        "core.AssistantConversation", on_delete=models.SET_NULL,
        null=True, blank=True, related_name="inquiries"
    )


    # MANAGEMENT

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    is_read = models.BooleanField(
        default=False
    )


    # TIMESTAMPS

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Contact Inquiry"

        verbose_name_plural = "Contact Inquiries"


    def __str__(self):

        return (
            f"{self.full_name} - "
            f"{self.get_service_display()}"
        )