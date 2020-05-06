'''
CRUD test on shorten models.

only C is tested, since we are using Django's build in models.Manage class
and only overwrite the create method
'''

from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import pytest

from . import URL, URL_SHORT
from .factory import (
    UrlFactory, 
    ShortCodeUrlFactory,
)
from shorten.models import Url


@pytest.mark.django_db(transaction=True)
class UrlCreateTestCase:
    '''Test Cases for Url Creation'''
    def test_url_defaults(db) ->  None:
        '''Test that default fields are working properly'''
        url: Url = ShortCodeUrlFactory()
        assert url.created
        assert url.modified
        assert url.created == url.modified
        assert url.redirect_count == 0

    def test_url_shortcode_is_primary(db) -> None:
        '''Test that Url field shortcode is primary key.'''
        UrlFactory()
        with pytest.raises(IntegrityError):
            ShortCodeUrlFactory(url=URL, shortcode=URL_SHORT)
            ShortCodeUrlFactory(url='google.com', shortcode=URL_SHORT)
        
        url: Url = ShortCodeUrlFactory(url='google.com', shortcode='goorgl')
        assert Url.objects.filter(pk=url.pk).exists()

    def test_url_autogenerate_shortcode(db) -> None:
        '''Test that Url short code is auto generated when None.'''
        url: Url = UrlFactory(url=URL)
        assert url.shortcode != None
        assert url.shortcode != URL_SHORT

    def test_increment_redirect_count(db):
        '''Test that rederect_count is auto-incremented and lat_redirect is monitoring redirect_count'''
        url: Url = UrlFactory()
        past = url.last_redirect
        assert url.redirect_count == 0
        url.increment_redirect_count()
        assert url.redirect_count == 1
        assert url.last_redirect != past


@pytest.mark.parametrize('value', [
    'abscew',
    'abd123',
    'ab__12',
    'ab__ab',
    '______',
    '123456',
])
def test_validate_shortcode_pass(value, db) -> None:
    '''Test shortcode regular expression validation happy path'''
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
    '''Test shortcode regular expression errors'''
    url = Url(url=URL, shortcode=value)
    with pytest.raises(ValidationError):
        url.full_clean()
