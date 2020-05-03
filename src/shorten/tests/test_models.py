from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import pytest

from . import URL, URL_SHORT
from .factory import (
    UrlFactory, 
    ShortCodeUrlFactory,
)
from ..models import Url


@pytest.mark.django_db(transaction=True)
class UrlCreateTestCase:
    def test_url_defaults(db) ->  None:
        url: Url = ShortCodeUrlFactory()
        assert url.created
        assert url.modified
        assert url.created == url.modified
        assert url.redirect_count == 0

    def test_url_unique(db) -> None:
        UrlFactory()
        with pytest.raises(IntegrityError):
            ShortCodeUrlFactory(url=URL, shortcode=URL_SHORT)
            ShortCodeUrlFactory(url='google.com', shortcode=URL_SHORT)
        
        url: Url = ShortCodeUrlFactory(url='google.com', shortcode='goorgl')
        assert Url.objects.filter(pk=url.pk).exists()

    def test_url_autogenerate_shortcode(db) -> None:
        url: Url = UrlFactory(url=URL)
        assert url.shortcode != None
        assert url.shortcode != URL_SHORT


@pytest.mark.parametrize('value', [
    'abscew',
    'abd123',
    'ab__12',
    'ab__ab',
    '______',
    '123456',
])
def test_validate_shortcode_pass(value, db) -> None:
    url = Url(url=URL, shortcode=value)
    if url.full_clean(): url.save()
    assert len(Url.objects.all()) == 0

@pytest.mark.parametrize('value', [
'AaaBbb',
'absc+w',
'ad-afa',
'aerfqwe',
'aergr',
'as 452',
'$asd89',
])
def test_validate_shortcode_error(value, db) ->  None:
    # with pytest.raises(ValidationError):
    url = Url(url=URL, shortcode=value)
    with pytest.raises(ValidationError):
        url.full_clean()
