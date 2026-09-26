from django.shortcuts import render, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Unit, Booking, BookingChangeRequest, UnitBlockedDate
from django.contrib.auth.models import User
from decimal import Decimal
from accounts.models import CustomerProfile


# Homepage
def index_view(request):
    units = Unit.objects.filter(active=True)
    return render(request, "index.html", {"units": units})


# Units
def units_list_view(request):
    units = Unit.objects.filter(active=True)
    return render(request, "bookings/units_list.html", {"units": units})


def unit_detail_view(request, unit_slug):
    unit = get_object_or_404(Unit, slug=unit_slug)

    bookings = Booking.objects.filter(unit=unit)

    booked_ranges = [
        {"start": b.check_in_date.isoformat(), "end": b.check_out_date.isoformat()}
        for b in bookings
    ]

    context = {
        "unit": unit,
        "booked_ranges": booked_ranges,
        "price_per_night": unit.price_per_night,
    }

    return render(request, "bookings/unit_detail.html", context)


# Booking Flow
@login_required
def booking_create_view(request, unit_slug):
    unit = get_object_or_404(Unit, slug=unit_slug)

    bookings = (
        Booking.objects.filter(unit=unit)
        .exclude(status="CANCELLED")
        .values(
            "check_in_date", "check_out_date"
        )
    )

    booked_ranges = []
    for b in bookings:
        booked_ranges.append(
            {
                "start": b["check_in_date"].strftime("%Y-%m-%d"),
                "end": b["check_out_date"].strftime("%Y-%m-%d"),
            }
        )

    blocked_dates = list(
        UnitBlockedDate.objects.filter(unit=unit)
        .values_list("date", flat=True)
    )
    blocked_dates = [
        blocked_date.isoformat() for blocked_date in blocked_dates
    ]

    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        adults = request.POST.get("adults")
        children = request.POST.get("children")
        dogs = request.POST.get("dogs")

        if not check_in or not check_out:
            messages.error(request, "Please select both check-in and check-out dates.")
            return redirect(request.path)

        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect(request.path)

        if check_out_date <= check_in_date:
            messages.error(request, "Check-out date must be after check-in date.")
            return redirect(request.path)

        if UnitBlockedDate.objects.filter(
            unit=unit,
            date__gte=check_in_date,
            date__lt=check_out_date,
        ).exists():
            messages.error(
                request,
                "This unit is unavailable for one or more selected nights.",
            )
            return redirect(request.path)

        overlapping = Booking.objects.filter(
            unit=unit,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date,
        ).exclude(status="CANCELLED")

        if overlapping.exists():
            messages.error(
                request, "This unit is not available for the selected dates."
            )
            return redirect(request.path)

        # Calculate nights
        nights = (check_out_date - check_in_date).days
        base_price = nights * unit.price_per_night

        # DOG SURCHARGE
        try:
            dog_count = int(dogs or 0)
        except (TypeError, ValueError):
            dog_count = 0

        dog_fee = (
            Decimal("20.00") if unit.dogs_allowed and dog_count > 0 else Decimal("0.00")
        )

        # Final total
        total_price = base_price + dog_fee

        # Who is making this booking?
        if request.user.is_staff:
            # Admin booking on behalf of a customer
            customer = None

            customer_name = request.POST.get("customer_name")
            customer_email = request.POST.get("customer_email")
            customer_phone = request.POST.get("customer_phone")
        else:
            # Customer booking themselves
            customer = request.user

            profile = CustomerProfile.objects.get(user=request.user)
            customer_name = profile.full_name
            customer_email = request.user.email
            customer_phone = profile.phone_number

        # Create booking
        booking = Booking.objects.create(
            unit=unit,
            customer=customer,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            adults=int(adults or 1),
            children=int(children or 0),
            dogs=dog_count,
            nightly_price=unit.price_per_night,
            total_nights=nights,
            dog_surcharge=dog_fee,
            total_amount=total_price,
            status="PENDING",
        )

        return redirect("my_bookings")

    return render(
        request,
        "bookings/booking_create.html",
        {
            "unit": unit,
            "booked_ranges": booked_ranges,
            "blocked_dates": blocked_dates,
        },
    )


# Customer Dashboard
@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(customer=request.user)

    for booking in bookings:
        booking.latest_request = (
            BookingChangeRequest.objects
            .filter(booking=booking)
            .order_by("-created_at")
            .first()
        )

    return render(
        request,
        "bookings/my_bookings.html",
        {"bookings": bookings},
    )

@login_required
def booking_detail_view(request, pk):
    booking = get_object_or_404(
        Booking,
        pk=pk,
        customer=request.user,
    )

    request_queryset = BookingChangeRequest.objects.filter(
        booking=booking,
        customer=request.user,
    )

    latest_request = request_queryset.order_by("-created_at", "-id").first()

    open_request = (
        request_queryset
        .filter(status="OPEN")
        .order_by("-created_at", "-id")
        .first()
    )

    return render(
        request,
        "bookings/booking_detail.html",
        {
            "booking": booking,
            "latest_request": latest_request,
            "open_request": open_request,
            "cancellation_requested": (
                open_request is not None
                and open_request.request_type == "CANCEL"
            ),
        },
    )

# UPDATED BOOKING UPDATE VIEW (no dashed lines)
@login_required
def booking_update_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)
    unit = booking.unit

    bookings = (
        Booking.objects.filter(unit=unit)
        .exclude(pk=booking.pk)
        .values("check_in_date", "check_out_date")
    )

    booked_ranges = []
    for b in bookings:
        booked_ranges.append(
            {
                "start": b["check_in_date"].strftime("%Y-%m-%d"),
                "end": b["check_out_date"].strftime("%Y-%m-%d"),
            }
        )

    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        adults = request.POST.get("adults")
        children = request.POST.get("children")
        dogs = request.POST.get("dogs")

        if not check_in or not check_out:
            messages.error(request, "Please select both check-in and check-out dates.")
            return redirect(request.path)

        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Invalid date format.")
            return redirect(request.path)

        if check_out_date <= check_in_date:
            messages.error(request, "Check-out date must be after check-in date.")
            return redirect(request.path)

        overlapping = (
            Booking.objects.filter(
                unit=unit,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date,
            )
            .exclude(pk=booking.pk)
            .exclude(status="CANCELLED")
        )

        if overlapping.exists():
            messages.error(
                request, "This unit is not available for the selected dates."
            )
            return redirect(request.path)

        try:
            dog_count = int(dogs or 0)
            adult_count = int(adults or 1)
            child_count = int(children or 0)

            if adult_count < 1 or child_count < 0 or dog_count < 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "Please enter valid guest numbers.")
            return redirect(request.path)

        BookingChangeRequest.objects.create(
            booking=booking,
            customer=request.user,
            request_type="MODIFY",
            message="Customer requested a booking modification.",
            status="OPEN",
            requested_check_in=check_in_date,
            requested_check_out=check_out_date,
            requested_adults=int(adults or 1),
            requested_children=int(children or 0),
            requested_dogs=dog_count,
        )

        messages.success(
            request,
            "Your modification request has been sent for admin approval.",
        )
        return redirect("booking_detail", pk=booking.pk)

    return render(
        request,
        "bookings/booking_update.html",
        {"booking": booking, "unit": unit, "booked_ranges": booked_ranges},
    )


# Booking Delete Requests
@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(
        Booking,
        pk=pk,
        customer=request.user,
    )

    if request.method == "POST":
        BookingChangeRequest.objects.get_or_create(
            booking=booking,
            customer=request.user,
            request_type="CANCEL",
            status="OPEN",
            defaults={"message": "Customer requested cancellation."},
        )

        return redirect("booking_detail", pk=booking.pk)

    return render(
        request,
        "bookings/booking_delete.html",
        {
            "booking": booking,
        },
    )

# Admin Dashboard
@login_required
def admin_bookings_list_view(request):
    if not request.user.is_staff:
        return render(request, "403.html")

    bookings = Booking.objects.all().order_by("check_in_date")

    for booking in bookings:
        booking.latest_request = (
            BookingChangeRequest.objects
            .filter(booking=booking)
            .order_by("-created_at")
            .first()
        )

    return render(
        request,
        "admin/admin_bookings_list.html",
        {"bookings": bookings},
    )

@login_required
def admin_booking_detail_view(request, pk):
    if not request.user.is_staff:
        return render(request, "403.html")

    booking = get_object_or_404(Booking, pk=pk)
    return render(request, "admin/admin_booking_detail.html", {"booking": booking})


@login_required
def admin_units_list_view(request):
    if not request.user.is_staff:
        return render(request, "403.html")

    units = Unit.objects.all()
    return render(request, "admin/admin_units_list.html", {"units": units})


@login_required
def admin_unit_detail_view(request, unit_slug):
    if not request.user.is_staff:
        return render(request, "403.html")

    unit = get_object_or_404(Unit, slug=unit_slug)
    return render(request, "admin/admin_unit_detail.html", {"unit": unit})


@login_required
def admin_customers_list_view(request):
    if not request.user.is_staff:
        return render(request, "403.html")

    customers = User.objects.all()
    return render(request, "admin/admin_customers_list.html", {"customers": customers})


@login_required
def admin_customer_detail_view(request, user_id):
    if not request.user.is_staff:
        return render(request, "403.html")

    customer = get_object_or_404(User, pk=user_id)
    bookings = Booking.objects.filter(customer=customer)
    return render(
        request,
        "admin/admin_customer_detail.html",
        {
            "customer": customer,
            "bookings": bookings,
        },
    )


def availability_calendar_view(request, unit_slug):
    unit = get_object_or_404(Unit, slug=unit_slug)

    bookings = Booking.objects.filter(unit=unit)

    booked_ranges = [
        {"start": b.check_in_date.isoformat(), "end": b.check_out_date.isoformat()}
        for b in bookings
    ]

    context = {
        "unit": unit,
        "booked_ranges": booked_ranges,
        "price_per_night": unit.price_per_night,
    }

    return render(request, "bookings/calendar.html", context)
