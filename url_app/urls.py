from django.conf.urls import url

from url_app.views import UrlShorterListCreateView, UrlShorterDeleteView

urlpatterns = [
    url(r'^urls/$', UrlShorterListCreateView.as_view()),
    url(r'^urls/(?P<pk>.+)/$', UrlShorterDeleteView.as_view()),
]
