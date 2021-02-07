from django import forms
from django.forms import ModelForm
from django.forms.fields import MultipleChoiceField
from .models import Post

from allauth.socialaccount import providers


class PostForm(ModelForm):
    choices = providers.registry.as_choices()
    # choices = (("twitter", "Twitter"), ("linkedin", "LinkedIn"), ("github", "Github"))
    providers = MultipleChoiceField(
        widget=forms.SelectMultiple, choices=choices, initial="1"
    )

    def clean_providers(self):
        return ",".join([str(p) for p in self.cleaned_data["providers"]])

    class Meta:
        model = Post
        fields = ["header", "content", "publish_on", "providers"]
