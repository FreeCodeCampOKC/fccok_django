from django.forms import forms, ModelForm
from django.forms.fields import MultipleChoiceField
from .models import Post

socials = (("twitter", "twitter"), ("linkedin", "linkedin"))


class PostForm(ModelForm):
    socials_list = MultipleChoiceField(choices=socials)

    class Meta:
        model = Post
        fields = ["header", "content", "publish_on"]
