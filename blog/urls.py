from django.urls import path

from . import views


app_name = "blog"


urlpatterns = [

    path(
        "",
        views.blog_list,
        name="blog_list"
    ),

    path(
        "subscribe/",
        views.newsletter_subscribe,
        name="newsletter_subscribe",
    ),


    path(
        "<slug:slug>/",
        views.blog_detail,
        name="blog_detail"
    ),
]
