from django.core.exceptions import ObjectDoesNotExist
from graphene import relay, Field, String
from graphql.execution.base import ResolveInfo

from .schema import UrlConnection, UrlType, UrlErrorUnion, HTTPErrorType
from .http_error import HTTP_NOT_FOUND
from ..models import Url


class UrlQuery:
    urls = relay.ConnectionField(UrlConnection)
    url = Field(UrlErrorUnion, shortcode=String())

    def resolve_urls(self, info: ResolveInfo, **kwargs):
        return Url.objects.all()

    def resolve_url(self, info: ResolveInfo, shortcode: String, **kwargs):
        try:
            url = Url.objects.get(shortcode=shortcode)
            url.increment_redirect_count()     
            return url
        except ObjectDoesNotExist:
            return HTTP_NOT_FOUND
