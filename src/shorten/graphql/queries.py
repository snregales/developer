from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from graphene import relay, Field, String
from graphql.execution.base import ResolveInfo

from .schema import UrlConnection, UrlType, UrlErrorUnion, HTTPErrorType
from .http_error import HTTP_NOT_FOUND
from shorten.models import Url


class UrlQuery:
    '''All url read queries.'''
    urls = relay.ConnectionField(UrlConnection)
    url = Field(UrlErrorUnion, shortcode=String())

    def resolve_urls(self, info: ResolveInfo, **kwargs) -> QuerySet:
        '''
        retreive all urls.
        
        :param info :type ResolveInfo
        :return :type QuerySet
        '''
        return Url.objects.all()

    def resolve_url(self, info: ResolveInfo, shortcode: str, **kwargs):
        '''
        retreive url by pk (shortcode)

        :param info :type ResolveInfo
        :param shortcode :type str
        :return :type Url
        '''
        try:
            url = Url.objects.get(shortcode=shortcode)
            url.increment_redirect_count()     
            return url
        except ObjectDoesNotExist:
            return HTTP_NOT_FOUND
