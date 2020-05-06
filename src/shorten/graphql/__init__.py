'''Shorten app graphql configurations'''

from typing import Dict, Union


ErrorMessage = Dict[str, Union[str, int]]

BAD: ErrorMessage = dict(
    message='Url not present or valid',
    code=400
) 

INVALID: ErrorMessage = dict(
    message='The provided shortcode is invalid', 
    code=412
)

IN_USE: ErrorMessage = dict(
    message='Shortcode already in use',
    code=409
)

NOT_FOUND: ErrorMessage = dict(
    message='Shortcode not found',
    code=404
)