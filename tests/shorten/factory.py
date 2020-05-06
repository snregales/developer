
from factory.django import DjangoModelFactory

from . import URL, URL_SHORT


class UrlFactory(DjangoModelFactory):
    '''Generate a Url object with default url field.'''
    class Meta:
        model = 'shorten.Url'
    
    url = URL

class ShortCodeUrlFactory(UrlFactory):
    '''Generate a Url object with default url and shortcode field.'''
    shortcode = URL_SHORT