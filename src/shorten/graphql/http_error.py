from .schema import HTTPErrorType
from . import INVALID, IN_USE, BAD, NOT_FOUND

HTTP_INVALID: HTTPErrorType = HTTPErrorType(**INVALID)
HTTP_IN_USE: HTTPErrorType = HTTPErrorType(**IN_USE)
HTTP_NOT_FOUND: HTTPErrorType = HTTPErrorType(**NOT_FOUND)
HTTP_BAD: HTTPErrorType = HTTPErrorType(**BAD)