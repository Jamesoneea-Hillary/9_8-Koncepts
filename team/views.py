from django.shortcuts import get_object_or_404, render

from .models import TeamMember


def team_list(request):
    members = TeamMember.objects.filter(
        is_active=True
    )

    featured_members = members.filter(
        is_featured=True
    )

    context = {
        "members": members,
        "featured_members": featured_members,
    }

    return render(
        request,
        "team/team_list.html",
        context
    )


def member_detail(request, pk):
    member = get_object_or_404(
        TeamMember,
        pk=pk,
        is_active=True
    )

    related_members = (
        TeamMember.objects
        .filter(
            is_active=True,
            role=member.role
        )
        .exclude(pk=member.pk)
    )

    context = {
        "member": member,
        "related_members": related_members,
    }

    return render(
        request,
        "team/partials/member_detail.html",
        context
    )
