from django.contrib import admin
from django.urls import include, path

from .views import home


urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
]
