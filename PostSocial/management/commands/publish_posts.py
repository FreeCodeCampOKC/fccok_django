from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import FieldDoesNotExist
from PostSocial.models import Post
from datetime import date


class Command(BaseCommand):
    help = "Publishes all posts in the database whose publish_on date is less than or equal to today and have not been published before."

    def handle(self, *args, **kwargs):
        try:
            # posts that haven't been published and publish_on is gte to today
            today = date.today()
            providers = ["twitter", "github"]
            publishable = Post.objects.filter(publish_on__lte=today, published=False)
            for post in publishable:
                for social in post.socials.split(","):
                    print(social)
                post.publish()
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully published {post.header}")
                )
        except FieldDoesNotExist:
            self.stdout.write(self.style.ERROR('Field "header" does not exist.'))
            return

        self.stdout.write(
            self.style.SUCCESS("Successfully published all publishable Posts")
        )
        return
