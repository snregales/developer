from datetime import datetime

from graphene.test import Client
import pytest

from config.graphql import schema

from shorten.graphql import NOT_FOUND
from . import ON_HTTP_ERROR_TYPE, ON_URL_TYPE
from ..factory import ShortCodeUrlFactory

def test_url_not_found(db) -> None:
    assert Client(schema).execute(
'''
{
    url(shortcode: "qwerty") {
    %s
  }
}
''' % ON_HTTP_ERROR_TYPE
    ) == {
    "data": {
      "url":  NOT_FOUND
    }
  }

@pytest.mark.django_db
def test_query_url(db) -> None:
    url = ShortCodeUrlFactory()
    response = Client(schema).execute(
'''
{
  url(shortcode: "%s") {
  %s
  }
} 
''' % (url.shortcode, ON_URL_TYPE)
    )
    assert response['data']['url']
    response = response['data']['url']
    assert response['url'] == url.url
    assert response['shortcode'] == url.shortcode
    assert datetime.fromisoformat(response['created']) == url.created
    assert datetime.fromisoformat(response['modified']) != url.modified
    assert datetime.fromisoformat(response['lastRedirect']) != url.last_redirect
    assert response['redirectCount'] == 1
