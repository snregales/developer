from django.db.utils import IntegrityError
import pytest

from . import URL, URL_SHORT
from .factory import UrlFactory
from ..models import Url

@pytest.mark.django_db(transaction=True)
class UrlCreateTestCase:
    def test_url_defaults(db) ->  None:
        url: Url = UrlFactory()
        assert url.created
        assert url.modified
        assert url.created == url.modified
        assert url.redirect_count == 0

    def test_url_unique(db) -> None:
        UrlFactory()
        with pytest.raises(IntegrityError):
            Url.objects.create(url=URL, shortcode=URL_SHORT)
            UrlFactory(url='google.com', shortcode=URL_SHORT)
        
        url: Url = UrlFactory(url='google.com', shortcode='google')
        assert Url.objects.filter(pk=url.pk).exists()
