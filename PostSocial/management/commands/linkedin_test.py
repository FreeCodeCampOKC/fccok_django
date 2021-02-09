from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import FieldDoesNotExist
from PostSocial.models import Post
from datetime import date
import requests
import json


class Command(BaseCommand):
    help = "Blah"

    def handle(self, *args, **kwargs):

        headers = {"Authorization": "Bearer Y0UR_4CCES5_T0K3N_HERE"}

        r = requests.get("https://api.linkedin.com/v2/me", headers=headers)

        print(json.dumps(r.json(), indent=2))

        # CLIENT_ID = "78hfehy7xkc0ow"
        # CLIENT_SECRET = "i2hQdErb1Sgv0Wlx"
        # REDIRECT_URL = "http://localhost:8000/callback"
        # SCOPES = "r_emailaddress,r_liteprofile,w_member_social"

        # url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URL}&scope={SCOPES}"

        # share_data = {
        #     "distribution": {"linkedInDistributionTarget": {}},
        #     "owner": "urn:li:person:324_kGGaLE",
        #     "subject": "Test Share Subject",
        #     "text": {"text": "Test Share!"},
        # }

        # r = requests.post("https://api.linkedin.com/v2/shares", data=share_data)

        # # r = requests.get(url)

        # # print(r.text)

        # self.stdout.write(self.style.SUCCESS("Eyyy"))

        # return

        # try:
        #     # posts that haven't been published and publish_on is gte to today
        #     today = date.today()
        #     providers = ["twitter", "github"]
        #     publishable = Post.objects.filter(publish_on__lte=today, published=False)
        #     for post in publishable:
        #         for social in post.socials.split(","):
        #             print(social)
        #         post.publish()
        #         self.stdout.write(
        #             self.style.SUCCESS(f"Successfully published {post.header}")
        #         )
        # except FieldDoesNotExist:
        #     self.stdout.write(self.style.ERROR('Field "header" does not exist.'))
        #     return

        # self.stdout.write(
        #     self.style.SUCCESS("Successfully published all publishable Posts")
        # )
