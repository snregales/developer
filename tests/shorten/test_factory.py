import pytest

from . import URL, URL_SHORT
from .factory import ShortCodeUrlFactory, UrlFactory
from shorten.models import Url


def test_url_shortcode_factory(db) -> None:
    url = ShortCodeUrlFactory()
    assert Url.objects.filter(pk=url.pk).exists()
    assert url.shortcode == URL_SHORT


def test_url_factory(db) -> None:
    assert len(Url.objects.all()) == 0 
    url = UrlFactory()
    assert Url.objects.filter(pk=url.pk).exists()
    assert url.shortcode != URL_SHORT