from django.core.validators import RegexValidator
from rest_framework import serializers

from url_app.models import UrlShorter
from url_app.utils import generate_unique_key


class UrlShorterSerializer(serializers.ModelSerializer):
    last_enter_url = serializers.CharField(validators=[RegexValidator(
        regex="^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")])

    class Meta:
        model = UrlShorter
        fields = ('url', 'key', 'last_enter_url')
        read_only_fields = ('key', 'url')

    def create(self, validated_data):
        key = generate_unique_key()
        last_enter_url = validated_data.pop('last_enter_url')
        url = self.get_standard_url(last_enter_url)
        if UrlShorter.objects.filter(url=url).exists():
            url_obj = UrlShorter.objects.get(url=url)
            url_obj.last_enter_url = last_enter_url
            url_obj.save()
        else:
            url_obj = UrlShorter.objects.create(url=url, key=key, last_enter_url=last_enter_url)
        return url_obj

    def get_standard_url(self, url):
        if url[:7].lower() == 'http://':
            url = url[7:]
        elif url[:8].lower() == 'https://':
            url = url[8:]
        if url[:4].lower() == 'www.':
            url = url[4:]
        return url
