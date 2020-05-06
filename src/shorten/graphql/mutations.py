from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import IntegrityError
from graphene import Mutation, Field, String
from graphql.execution.base import ResolveInfo

from .http_error import HTTP_BAD, HTTP_IN_USE, HTTP_INVALID, HTTP_NOT_FOUND 
from .schema import UrlErrorUnion, HTTPErrorType
from .. import REGEX_VALIDATOR_MSG
from shorten.models import Url


class CreateUrl(Mutation):
    '''Url's creation mutation.'''
    class Arguments:
        url = String(required=True)
        shortcode = String()

    url = Field(UrlErrorUnion)
    
    def mutate(self, info: ResolveInfo, url: str, shortcode: str):
        '''
        Create a new instance and return its ObjectType

        :param info :type ResolveInfo
        :param url :type str
        :param shortcode :type str
        :return :type CreateUrl
        '''
        try:
            url_object = Url(url=url, shortcode=shortcode)
            url_object.full_clean()
            url_object.save()    
            return CreateUrl(url=url_object)
        except ValidationError as e:
            if 'url' in e.message_dict:
                return CreateUrl(HTTP_BAD)
            return CreateUrl(
                url=HTTP_INVALID if e.messages[0] == REGEX_VALIDATOR_MSG else HTTP_IN_USE
            )


class UpdateUrl(Mutation):
    '''Url's update mutation'''
    class Arguments:
        url = String()
        id = String(required=True)

    url = Field(UrlErrorUnion)

    def mutate(self, info:ResolveInfo, id: str, url: str):
        '''
        Get instance by id and update its url.

        :param info :type ResolveInfo
        :param id :type str
        :param url :type str
        :return :type UpdateUrl
        '''
        try:
            url_object = Url.objects.get(pk=id)
            url_object.url = url
            url_object.save()
            return UpdateUrl(url=url_object)
        except ObjectDoesNotExist:
            return UpdateUrl(url=HTTP_NOT_FOUND)
            

class DeleteUrl(Mutation):
    '''Url's delete matation'''
    class Arguments:
        id = String(required=True)

    url = Field(UrlErrorUnion)

    def mutate(self, info:ResolveInfo, id: str):
        '''
        Get instance by id and remove it.

        :param info :type ResolveInfo
        :param id :type str
        :return :type DeleteUrl
        '''
        try:
            url = Url.objects.get(pk=id)
            url.delete()
            return DeleteUrl(url=url)
        except ObjectDoesNotExist:
            return DeleteUrl(url=HTTP_NOT_FOUND)


class UrlMutations:
    '''All of Url's mutations'''
    create_url = CreateUrl.Field()
    update_url = UpdateUrl.Field()
    delete_url = DeleteUrl.Field()
