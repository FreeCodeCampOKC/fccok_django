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
        print(postform.is_valid())
        if postform.is_valid():
            print(postform.cleaned_data["providers"])
            postform.save()
            return redirect("posts")
    else:
        postform = PostForm()
    return render(request, "post_form.html", {"post": postform})
