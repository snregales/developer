from .schema import HTTPErrorType

INVALID: HTTPErrorType = HTTPErrorType( 
    message='The provided shortcode is invalid', 
    code=412
)
IN_USE: HTTPErrorType = HTTPErrorType(
    message='Shortcode already in use',
    code=409
)
NOT_FOUND: HTTPErrorType = HTTPErrorType(
    message='Shortcode not found',
    code=404
)
BAD: HTTPErrorType = HTTPErrorType( 
    message='Url not present or valid',
    code=400
)