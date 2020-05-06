import pytest

from shorten.utils import (
    generate_shortcode, 
)

def test_generated_shortcode() -> None:
    '''Test that generated shortcode is a random 6 alpha numeric character.'''
    short = generate_shortcode()
    assert len(short) == 6
    assert short.isalnum
    assert short.islower
    assert short.isascii
    assert short != generate_shortcode()
