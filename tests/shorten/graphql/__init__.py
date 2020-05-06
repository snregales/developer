ON_URL_TYPE: str = '''
... on UrlType {
    url
    shortcode
    lastRedirect
    created
    modified
    redirectCount      
}
'''
ON_HTTP_ERROR_TYPE: str = '''
... on HTTPErrorType {
    message
    code
}
'''