from django.utils.crypto import get_random_string

from url_app.models import UrlShorter


def generate_unique_key():
    while True:
        key = get_random_string(length=5)
        if not UrlShorter.objects.filter(key=key).exists():
            return key