from django.urls import path

from .views import (
    PollCreateView,
    PollDeleteView,
    PollUpdateView,
    PollDetailView,
    PollListView,
)

urlpatterns = [
    path("create/", PollCreateView.as_view(), name="poll_create"),
    path("<int:pk>/delete/", PollDeleteView.as_view(), name="poll_delete"),
    path("<int:pk>/update/", PollUpdateView.as_view(), name="poll_update"),
    path("<int:pk>/", PollDetailView.as_view(), name="poll_detail"),
    path("", PollListView.as_view(), name="poll_list"),
]
