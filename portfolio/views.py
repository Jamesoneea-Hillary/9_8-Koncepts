from django.shortcuts import (
    render,
    get_object_or_404,
)

from .models import (
    Project,
    ProjectCategory,
)


def portfolio_list(request):

    projects = (
        Project.objects
        .select_related(
            "category"
        )
        .prefetch_related(
            "technologies"
        )
    )

    categories = (
        ProjectCategory.objects
        .all()
    )

    context = {
        "projects": projects,
        "categories": categories,
    }

    return render(
        request,
        "portfolio/portfolio_list.html",
        context
    )


def portfolio_detail(
    request,
    slug
):

    project = get_object_or_404(

        Project.objects
        .select_related(
            "category"
        )
        .prefetch_related(
            "technologies",
            "images"
        ),

        slug=slug
    )

    related_projects = (
        Project.objects
        .filter(
            category=project.category
        )
        .exclude(
            id=project.id
        )
        .select_related(
            "category"
        )
        .prefetch_related(
            "technologies"
        )
        [:3]
    )

    context = {
        "project": project,
        "related_projects": related_projects,
    }

    return render(
        request,
        "portfolio/portfolio_detail.html",
        context
    )