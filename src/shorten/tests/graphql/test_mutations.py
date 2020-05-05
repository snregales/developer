from datetime import datetime

from graphene.test import Client

from config.graphql import schema
from shorten.graphql import BAD, IN_USE, INVALID, NOT_FOUND
from shorten.models import Url

from . import ON_HTTP_ERROR_TYPE, ON_URL_TYPE
from .. import URL, URL_SHORT
from ..factory import ShortCodeUrlFactory

def test_create_url(db) -> None:
    response = Client(schema=schema).execute(
'''
mutation {
  createUrl(shortcode: "%s", url:"%s"){
    url {
      %s
    }
  }
}
''' % (URL_SHORT, URL, ON_URL_TYPE))
    print(response)
    assert response['data']['createUrl']['url']
    response = response['data']['createUrl']['url']
    assert response['url'] ==  URL
    assert response['shortcode'] == URL_SHORT
    assert response['redirectCount'] == 0


def test_create_url_bad(db) -> None:
    Client(schema=schema).execute(
'''
mutation {
  createUrl(shortcode: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % (URL_SHORT, 'jack,com', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "createUrl": {
                "url": BAD
            } 
        }
    }


def test_create_already_in_use(db) -> None:
    ShortCodeUrlFactory()
    Client(schema=schema).execute(
'''
mutation {
  createUrl(shortcode: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % (URL_SHORT, 'https://jack.com', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "createUrl": {
                "url": IN_USE
            } 
        }
    }
  

def test_create_already_invalid(db) -> None:
    Client(schema=schema).execute(
'''
mutation {
  createUrl(shortcode: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % ('sjafqwe', 'https://jack.com', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "createUrl": {
                "url": INVALID
            } 
        }
    }


def test_update_url(db) -> None:
    url = ShortCodeUrlFactory()
    assert url.url != 'https://jack.com'
    response = Client(schema=schema).execute(
'''
mutation {
  updateUrl(id: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % (url.shortcode, 'https://jack.com', ON_URL_TYPE)
    )
    assert response['data']['updateUrl']['url']
    response = response['data']['updateUrl']['url']
    assert response['url'] == 'https://jack.com'
    assert response['shortcode'] == url.shortcode
    assert datetime.fromisoformat(response['created']) == url.created
    assert datetime.fromisoformat(response['modified']) != url.modified
    assert datetime.fromisoformat(response['lastRedirect']) == url.last_redirect
    assert response['redirectCount'] == 0
    

def test_update_not_found(db) -> None:
    ShortCodeUrlFactory()
    Client(schema=schema).execute(
'''
mutation {
  updateUrl(id: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % ('sjafqwe', 'https://jack.com', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "createUrl": {
                "url": NOT_FOUND
            } 
        }
    }


def test_update_bad(db) -> None:
    ShortCodeUrlFactory()
    Client(schema=schema).execute(
'''
mutation {
  updateUrl(id: "%s", url:"%s"){
	url{
      %s
    }	
  }
}
''' % (URL_SHORT, 's://jack.com', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "createUrl": {
                "url": BAD 
            } 
        }
    }


def test_delete(db) -> None:
    url = ShortCodeUrlFactory()
    Client(schema=schema).execute(
'''
mutation {
  deleteUrl(id: "%s"){
	url{
        %s
    }	
  }
}
''' % (URL_SHORT, ON_URL_TYPE)
    )
    assert not Url.objects.filter(pk=url.shortcode).exists()


def test_delete_not_found(db) -> None:
    url = ShortCodeUrlFactory()
    assert Client(schema=schema).execute(
'''
mutation {
  deleteUrl(id: "%s"){
	url{
      %s
    }	
  }
}
''' % ('qwerty', ON_HTTP_ERROR_TYPE)
    ) == {
        "data": {
            "deleteUrl": {
                "url": NOT_FOUND 
            } 
        }
    }
    assert Url.objects.filter(pk=url.shortcode).exists()
