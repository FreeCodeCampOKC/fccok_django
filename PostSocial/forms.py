from django import forms
from django.forms import ModelForm
from django.forms.fields import MultipleChoiceField
from .models import Post

from allauth.socialaccount import providers


class PostForm(ModelForm):
    choices = providers.registry.as_choices()
    # choices = (("twitter", "Twitter"), ("linkedin", "LinkedIn"), ("github", "Github"))
    providers = MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={"class": "form-select"}),
        choices=choices,
        initial="1",
    )

    def clean_providers(self):
        return ",".join([str(p) for p in self.cleaned_data["providers"]])

    class Meta:
        model = Post
        fields = ["header", "content", "publish_on", "providers"]
        widgets = {
            "header": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "publish_on": forms.DateInput(attrs={"class": "form-control"}),
            "providers": forms.SelectMultiple(attrs={"class": "form-select"}),
        }
