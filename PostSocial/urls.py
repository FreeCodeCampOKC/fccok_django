from django.urls import path
from .views import Posts, Messages, AuthorizedUserPost, LinkedInCallback

app_name = "PostSocial"
urlpatterns = [
    path("", Posts, name="posts"),
    path("messages", Messages, name="messages"),
    path("authorized-post", AuthorizedUserPost, name="authorized-post"),
    path("callback", LinkedInCallback, name="linkedin-callback"),
]
