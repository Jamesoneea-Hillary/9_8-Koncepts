from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

from .models import (
    BlogPost,
    Category,
    NewsletterSubscriber,
)
from .forms import NewsletterSubscriptionForm


def blog_list(request):

    posts = (
        BlogPost.objects
        .filter(
            status="published"
        )
        .select_related(
            "category",
            "author"
        )
        .prefetch_related(
            "tags"
        )
    )


    featured_post = (
        posts
        .filter(
            is_featured=True
        )
        .first()
    )


    categories = Category.objects.all()


    query = request.GET.get(
        "q"
    )


    category_slug = request.GET.get(
        "category"
    )


    if query:

        posts = posts.filter(

            Q(
                title__icontains=query
            )

            |

            Q(
                excerpt__icontains=query
            )

            |

            Q(
                content__icontains=query
            )

        )


    if category_slug:

        posts = posts.filter(

            category__slug=
            category_slug

        )


    paginator = Paginator(
        posts,
        9
    )


    page_number = request.GET.get(
        "page"
    )


    page_obj = paginator.get_page(
        page_number
    )


    context = {

        "page_obj":
        page_obj,

        "posts":
        page_obj,

        "featured_post":
        featured_post,

        "categories":
        categories,

        "query":
        query,

        "selected_category":
        category_slug,

    }


    return render(
        request,
        "blog/blog_list.html",
        context
    )


def blog_detail(
    request,
    slug
):

    post = get_object_or_404(

        BlogPost.objects
        .select_related(
            "category",
            "author"
        )
        .prefetch_related(
            "tags"
        ),

        slug=slug,

        status="published"

    )


    related_posts = (

        BlogPost.objects

        .filter(
            status="published",
            category=post.category
        )

        .exclude(
            id=post.id
        )

        .select_related(
            "category",
            "author"
        )[:3]

    )


    context = {

        "post":
        post,

        "related_posts":
        related_posts,

    }


    return render(
        request,
        "blog/blog_detail.html",
        context
    )


@require_POST
def newsletter_subscribe(request):

    form = NewsletterSubscriptionForm(request.POST)

    if form.is_valid():
        subscriber, created = NewsletterSubscriber.objects.get_or_create(
            email=form.cleaned_data["email"]
        )

        if created:
            messages.success(
                request,
                "Thanks for subscribing. You are on the list for future updates.",
            )
        elif subscriber.is_active:
            messages.info(
                request,
                "That email address is already subscribed.",
            )
        else:
            subscriber.is_active = True
            subscriber.save(update_fields=["is_active"])
            messages.success(
                request,
                "Your newsletter subscription has been reactivated.",
            )
    else:
        for error_list in form.errors.values():
            for error in error_list:
                messages.error(request, error)

    return redirect(f"{reverse('blog:blog_list')}#newsletter")
