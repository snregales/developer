import pytest

from . import URL, URL_SHORT
from .factory import ShortCodeUrlFactory
from ..models import Url


@pytest.mark.django_db
def test_url_factory(db) -> None:
    assert len(Url.objects.all()) == 0 
    url = ShortCodeUrlFactory()
    assert Url.objects.filter(pk=url.pk).exists()
    assert url.shortcode == URL_SHORT