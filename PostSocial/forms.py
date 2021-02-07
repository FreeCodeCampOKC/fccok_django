from django import forms
from django.forms import ModelForm
from django.forms.fields import MultipleChoiceField
from .models import Post

from allauth.socialaccount import providers


class PostForm(ModelForm):
    # choices = ((str(i), v[0]) for i, v in enumerate(providers.registry.as_choices()))
    choices = ((1, "Twitter"), (2, "LinkedIn"), (3, "Github"))
    providers = MultipleChoiceField(
        widget=forms.SelectMultiple, choices=choices, initial="1"
    )

    def clean_providers(self):
        return ",".join([str(p) for p in self.cleaned_data["providers"]])

    class Meta:
        model = Post
        fields = ["header", "content", "publish_on", "providers"]
