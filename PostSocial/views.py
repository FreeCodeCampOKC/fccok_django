from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post

from .forms import PostForm

# Create your views here.
@login_required
@user_passes_test(lambda user: user.is_staff)
def Posts(request):

    posts = Post.objects.all()
    return render(request, "PostSocial/posts.html", {"posts": posts})


def Messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

    return HttpResponse("Messages added", content_type="text/plain")


def AuthorizedUserPost(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        socials = dict(postform.data).get("socials_list")
        print(socials)
        socials = ",".join(socials)
        post = Post()
        post.header = dict(postform.data).get("header")[0]
        post.content = dict(postform.data).get("content")[0]
        post.socials = socials
        post.save()
        return redirect("posts")
    else:
        post = PostForm()
    return render(request, "post_form.html", {"post": post})
