# from django.core.exceptions import ValidationError
import pytest

from ..utils import (
    generate_shortcode, 
    # validate_shortcode,
)

def test_generated_shortcode() -> None:
    short = generate_shortcode()
    assert len(short) == 6
    assert short.isalnum
    assert short.islower
    assert short.isascii


