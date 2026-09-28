from bookings.models import Booking, UnitBlockedDate


def validate_booking_change(
    *,
    unit,
    check_in,
    check_out,
    adults,
    children,
    exclude_booking_id=None,
):
    """Return a user-facing validation error, or None when the change is valid."""
    if check_out <= check_in:
        return "Check-out date must be after check-in date."

    nights = (check_out - check_in).days
    if nights < 2:
        return "Minimum stay is 2 nights."

    if adults < 1 or children < 0:
        return "Please enter valid guest numbers."

    if adults > unit.max_adults or children > unit.max_children:
        return (
            f"This unit allows up to {unit.max_adults} adults and "
            f"{unit.max_children} children."
        )

    if UnitBlockedDate.objects.filter(
        unit=unit,
        date__gte=check_in,
        date__lt=check_out,
    ).exists():
        return "This unit is unavailable for one or more selected nights."

    overlapping = Booking.objects.filter(
        unit=unit,
        check_in_date__lt=check_out,
        check_out_date__gt=check_in,
    ).exclude(status="CANCELLED")

    if exclude_booking_id is not None:
        overlapping = overlapping.exclude(pk=exclude_booking_id)

    if overlapping.exists():
        return "This unit is not available for the selected dates."

    return None