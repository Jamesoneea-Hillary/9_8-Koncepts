from django.db import models
from django.utils.text import slugify


class ProjectCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Technology(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Bootstrap icon class e.g. bi bi-filetype-py"
    )

    logo = models.ImageField(
        upload_to="portfolio/technologies/",
        blank=True,
        null=True
    )

    class Meta:

        ordering = [
            "name"
        ]

    def __str__(self):

        return self.name


class Project(models.Model):

    STATUS_CHOICES = (
        ("completed", "Completed"),
        ("ongoing", "Ongoing"),
        ("maintenance", "Under Maintenance"),
    )

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="projects"
    )

    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="projects"
    )

    short_description = models.TextField(
        max_length=300,
        help_text="A short description for project cards."
    )

    description = models.TextField(
        help_text="Detailed project description."
    )

    client = models.CharField(
        max_length=150,
        blank=True
    )

    project_url = models.URLField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="portfolio/projects/"
    )

    is_featured = models.BooleanField(
        default=False
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="completed"
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

        ordering = [
            "display_order",
            "-created_at"
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="portfolio/project_images/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:

        ordering = [
            "display_order"
        ]

    def __str__(self):

        return f"Image for {self.project.title}"