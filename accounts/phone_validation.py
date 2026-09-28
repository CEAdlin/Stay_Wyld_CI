def normalize_phone_number(value):
    """Return an 11-digit phone number without spaces, or None if invalid."""
    normalized = "".join((value or "").split())

    if not normalized.isdigit() or len(normalized) != 11:
        return None

    return normalized