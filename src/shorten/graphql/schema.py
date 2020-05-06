from typing import Union

from graphene import (
    relay, 
    String, 
    Int, 
    Union as GraphUnion,
    ObjectType,
)
from graphene_django import DjangoObjectType
from graphql.execution.base import ResolveInfo
from shorten.models import Url


class HTTPErrorType(ObjectType):
    message = String()
    code = Int()


class UrlType(DjangoObjectType):
    redirect_count = Int()
    class Meta:
        model = Url
        exclude = ('_redirect_count',)
        interface = (relay.Node)


class UrlErrorUnion(GraphUnion):
    """UrlErrorUnion is a graphene.union of HTTPErrorType and UrlType"""
    class Meta:
        types = (HTTPErrorType, UrlType)


class UrlConnection(relay.Connection):
    '''UrlConnection is a relay.Connection of UrlType'''
    class Meta:
        node = UrlType