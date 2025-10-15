import secrets
import string
from datetime import datetime
from typing import Optional


def generate_code(
    prefix: str = "SP",
    embed_date: bool = True,
    date_dt: Optional[datetime] = None,
    date_format: str = "%d%m%y",
    mid_letters: int = 3,
    mid_digits: int = 1,
    suffix_letters: int = 2,
) -> str:
    """
    Generate a code like: <prefix><date><mid_letters><mid_digits><suffix_letters>
    Example: DI121025EDJ7CQ
    - Uses secrets.choice for cryptographic randomness.
    - All letters are uppercase.
    - If embed_date is False, the date slot will be filled with random digits of same length.
    """
    _letters = string.ascii_uppercase
    _digits = string.digits
    prefix = (prefix or "").upper()

    if embed_date:
        dt = date_dt or datetime.utcnow()
        date_part = dt.strftime(date_format)
    else:
        date_part = "".join(
            secrets.choice(_digits)
            for _ in range(len(datetime.utcnow().strftime(date_format)))
        )

    mid_letters_part = "".join(secrets.choice(_letters) for _ in range(mid_letters))
    mid_digits_part = "".join(secrets.choice(_digits) for _ in range(mid_digits))
    suffix_part = "".join(secrets.choice(_letters) for _ in range(suffix_letters))

    return f"{prefix}{date_part}{mid_letters_part}{mid_digits_part}{suffix_part}"
