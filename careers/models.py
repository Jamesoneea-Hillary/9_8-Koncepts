from django.db import models
from django.urls import reverse


class JobOpening(models.Model):

    EMPLOYMENT_TYPES = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
        ("internship", "Internship"),
        ("freelance", "Freelance"),
    ]

    WORK_MODES = [
        ("onsite", "On-site"),
        ("remote", "Remote"),
        ("hybrid", "Hybrid"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True
    )

    department = models.CharField(
        max_length=100
    )

    employment_type = models.CharField(
        max_length=30,
        choices=EMPLOYMENT_TYPES,
        default="full_time"
    )

    work_mode = models.CharField(
        max_length=20,
        choices=WORK_MODES,
        default="onsite"
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    short_description = models.TextField(
        max_length=400
    )

    description = models.TextField()

    responsibilities = models.TextField(
        help_text="Enter each responsibility on a new line."
    )

    requirements = models.TextField(
        help_text="Enter each requirement on a new line."
    )

    nice_to_have = models.TextField(
        blank=True,
        help_text="Enter each additional skill on a new line."
    )

    application_deadline = models.DateField(
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "-is_featured",
            "-created_at",
        ]

        verbose_name = "Job Opening"
        verbose_name_plural = "Job Openings"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "careers:job_detail",
            kwargs={"slug": self.slug}
        )

    @property
    def responsibility_list(self):
        return [
            item.strip()
            for item in self.responsibilities.splitlines()
            if item.strip()
        ]

    @property
    def requirement_list(self):
        return [
            item.strip()
            for item in self.requirements.splitlines()
            if item.strip()
        ]

    @property
    def nice_to_have_list(self):
        return [
            item.strip()
            for item in self.nice_to_have.splitlines()
            if item.strip()
        ]


class JobApplication(models.Model):

    job = models.ForeignKey(
        JobOpening,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    full_name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30
    )

    cover_letter = models.TextField()

    resume = models.FileField(
        upload_to="careers/resumes/"
    )

    portfolio_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"

    def __str__(self):
        return f"{self.full_name} — {self.job.title}"