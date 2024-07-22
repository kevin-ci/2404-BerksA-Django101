from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("<article_id>", views.view_article),
]