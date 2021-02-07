from allauth.socialaccount import providers
from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django_extensions.db.models import TimeStampedModel
from crum import get_current_user
from django.utils.text import slugify

# Create your models here.


class Post(TimeStampedModel):

    header = models.CharField(_("header"), max_length=100, blank=True)
    content = models.CharField(_("Content"), max_length=500)
    publish_on = models.DateTimeField(_("Publish Date"), null=True, blank=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    socials = models.TextField(_("Socials"))  # comma separated providers
    providers = models.TextField(
        _("Providers"),
        default="",
        blank=False,
        max_length=50,
        # validators=[validate_comma_separated_integer_list],
    )
    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
        related_name="created_post",
    )
    modified_by = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        default=None,
        blank=True,
        null=True,
        related_name="modified_post",
    )

    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        if kwargs.get("system"):
            del kwargs["system"]
            super(Post, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.header)
            user = get_current_user()
            if user and not user.pk:
                user = None  # annonymous django user
            if not self.pk:  # new Post
                self.created_by = user
            self.modified_by = user
            super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        publish = ""
        if self.published:
            publish = "published"
        else:
            publish = "not published"
        return f"{self.header} - {publish} - {self.publish_on}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def publish(self):
        self.published = True
        self.save(system=True)
