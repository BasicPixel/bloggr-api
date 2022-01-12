from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("posts", views.posts),
    path("post/<int:id>", views.post),
    path("add-post", views.add_post),
    path("update/<int:id>", views.update_post),
    path("delete/<int:id>", views.delete_post),
]
