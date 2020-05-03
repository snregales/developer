from random import SystemRandom
from string import ascii_lowercase, digits


def generate_shortcode() -> str:
    """Generate random 6 alpha numeric lowercase character string."""
    return "".join(
        map(lambda x: SystemRandom().choice(ascii_lowercase + digits), range(6))
    )
