from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        verbose_name = "Category"

        verbose_name_plural = "Categories"

        ordering = ["name"]


    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                self.name
            )

        super().save(
            *args,
            **kwargs
        )


    def __str__(self):

        return self.name

class Tag(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True
    )

    slug = models.SlugField(
        max_length=70,
        unique=True,
        blank=True
    )


    class Meta:

        ordering = ["name"]


    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                self.name
            )

        super().save(
            *args,
            **kwargs
        )


    def __str__(self):

        return self.name

class BlogPost(models.Model):

    STATUS_CHOICES = [

        ("draft", "Draft"),

        ("published", "Published"),

    ]


    title = models.CharField(
        max_length=250
    )


    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True
    )


    excerpt = models.TextField(
        max_length=500,
        help_text=(
            "A short summary displayed "
            "on the blog listing page."
        )
    )


    content = models.TextField()


    featured_image = models.ImageField(
        upload_to="blog/posts/",
        blank=True,
        null=True
    )


    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        blank=True
    )


    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        blank=True
    )


    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
        blank=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )


    is_featured = models.BooleanField(
        default=False
    )


    published_at = models.DateTimeField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        ordering = [
            "-published_at",
            "-created_at"
        ]


        verbose_name = "Blog Post"

        verbose_name_plural = "Blog Posts"


    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(
                self.title
            )

        super().save(
            *args,
            **kwargs
        )


    def __str__(self):

        return self.title


class NewsletterSubscriber(models.Model):

    email = models.EmailField(
        unique=True
    )

    subscribed_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-subscribed_at"]
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

    def __str__(self):
        return self.email
