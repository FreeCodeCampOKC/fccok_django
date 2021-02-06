from django.urls import path
from .views import Posts, Messages, AuthorizedUserPost

urlpatterns = [
    path("", Posts, name="posts"),
    path("messages", Messages, name="messages"),
    path("authorized-post", AuthorizedUserPost, name="authorized-post"),
]
