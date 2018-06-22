# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import redirect
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveAPIView

from url_app.models import UrlShorter
from url_app.serializers import UrlShorterSerializer


class UrlShorterListCreateView(ListCreateAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()


class UrlShorterDeleteView(DestroyAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()


class UrlRedirectorView(RetrieveAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = UrlShorterSerializer
    queryset = UrlShorter.objects.all()

    def retrieve(self, request, *args, **kwargs):
        url = self.get_object()
        return redirect("//" + url.url)
