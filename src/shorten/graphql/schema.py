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
from ..models import Url


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
    """ProtectedUnion is a union between MessageField and AuthInfoField."""

    class Meta:
        """Tels the api user what to expect from this object."""

        types = (HTTPErrorType, UrlType)


class UrlConnection(relay.Connection):
    class Meta:
        node = UrlType