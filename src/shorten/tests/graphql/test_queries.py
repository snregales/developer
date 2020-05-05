from datetime import datetime

from graphene.test import Client
import pytest

from config.graphql import schema

from ..factory import ShortCodeUrlFactory


def test_url_not_found(db) -> None:
    assert Client(schema).execute(
'''
{
    url(shortcode: "qwerty") {
    __typename
    ... on UrlType {
      shortcode
      lastRedirect
    }
    ... on HTTPErrorType {
      message
      code
    }
  }
}
'''
    ) == {
    "data": {
        "url": {
        "__typename": "HTTPErrorType",
        "message": "Shortcode qwerty not found",
        "code": 404
        }
    }
}

@pytest.mark.django_db
def test_query_url(db) -> None:
    url = ShortCodeUrlFactory()
    response = Client(schema).execute(
'''
{
  url(shortcode: "%s") {
    __typename
    ... on UrlType {
      url
      shortcode
      lastRedirect
      created
      modified
      redirectCount      
    }
    ... on HTTPErrorType {
      message
      code
    }
  }
} 
''' % url.shortcode
    )
    assert response['data']['url']
    response = response['data']['url']
    assert response['url'] == url.url
    assert response['shortcode'] == url.shortcode
    assert datetime.fromisoformat(response['created']) == url.created
    assert datetime.fromisoformat(response['modified']) != url.modified
    assert datetime.fromisoformat(response['lastRedirect']) != url.last_redirect
    assert response['redirectCount'] == 1
