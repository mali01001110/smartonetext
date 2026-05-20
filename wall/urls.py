from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("feed/", views.feed, name="feed"),
    path("messages/<int:message_id>/delete/", views.delete_message, name="delete_message"),
]