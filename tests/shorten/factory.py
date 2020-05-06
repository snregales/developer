
from factory.django import DjangoModelFactory

from . import URL, URL_SHORT


class UrlFactory(DjangoModelFactory):
    class Meta:
        model = 'shorten.Url'
    
    url = URL

class ShortCodeUrlFactory(UrlFactory):
    shortcode = URL_SHORT