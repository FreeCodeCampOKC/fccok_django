from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Post
import requests

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


def LinkedInCallback(request):
    """
    1. Have the server running
    2. Paste this URL into your browser: https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=78hfehy7xkc0ow&redirect_uri=http://localhost:8000/callback&scope=r_emailaddress,r_liteprofile,w_member_social
    3. Follow browser prompts until you see your access token
    4. Copy your access token into PostSocial/management/commands/linkedin_test.py into the `headers` dictionary
    5. Run `python manage.py linkedin_test` to test if the code works
    """

    code = request.GET.get("code")
    CLIENT_ID = "78hfehy7xkc0ow"
    CLIENT_SECRET = "i2hQdErb1Sgv0Wlx"
    REDIRECT_URL = "http://localhost:8000/callback"

    if code:
        print("authorization code: " + code)
    else:
        print("second time")

    url = f"https://linkedin.com/oauth/v2/accessToken?grant_type=authorization_code&code={code}&redirect_uri={REDIRECT_URL}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"

    r = requests.post(url)

    return JsonResponse(r.json())