from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("chatbot/reply/", views.chatbot_reply, name="chatbot_reply"),
    path("chatbot/inquiry/", views.assistant_inquiry, name="assistant_inquiry"),
]
