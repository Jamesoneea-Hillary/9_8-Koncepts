from django.urls import path

from . import views


app_name = "careers"


urlpatterns = [

    path(
        "",
        views.careers_list,
        name="careers_list"
    ),

    path(
        "application/success/",
        views.application_success,
        name="application_success"
    ),

    path(
        "<slug:slug>/apply/",
        views.apply_for_job,
        name="apply_for_job"
    ),

    path(
        "<slug:slug>/",
        views.job_detail,
        name="job_detail"
    ),
]