from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Unit, Booking, BookingChangeRequest
from django.contrib.auth.models import User
from decimal import Decimal


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

    bookings = Booking.objects.filter(unit=unit).values(
        "check_in_date",
        "check_out_date"
    )

    booked_ranges = []
    for b in bookings:
        booked_ranges.append({
            "start": b["check_in_date"].strftime("%Y-%m-%d"),
            "end": b["check_out_date"].strftime("%Y-%m-%d")
        })

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

        overlapping = Booking.objects.filter(
            unit=unit,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        )

        if overlapping.exists():
            messages.error(request, "This unit is not available for the selected dates.")
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
            Decimal("20.00")
            if unit.dogs_allowed and dog_count > 0
            else Decimal("0.00")
        )

        # Final total
        total_price = base_price + dog_fee

        # Create booking
        booking = Booking.objects.create(
            unit=unit,
            customer=request.user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            adults=adults,
            children=children,
            dogs=dogs,
            nightly_price=unit.price_per_night,
            total_nights=nights,
            dog_surcharge=dog_fee,
            total_amount=total_price,
            status="PENDING"
        )

        return redirect("my_bookings")

    return render(request, "bookings/booking_create.html", {
        "unit": unit,
        "booked_ranges": booked_ranges
    })

# Customer Dashboard
@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})


@login_required
def booking_detail_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)
    return render(request, "bookings/booking_detail.html", {"booking": booking})


# UPDATED BOOKING UPDATE VIEW (no dashed lines)
@login_required
def booking_update_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)
    unit = booking.unit

    bookings = Booking.objects.filter(unit=unit).exclude(pk=booking.pk).values(
        "check_in_date",
        "check_out_date"
    )

    booked_ranges = []
    for b in bookings:
        booked_ranges.append({
            "start": b["check_in_date"].strftime("%Y-%m-%d"),
            "end": b["check_out_date"].strftime("%Y-%m-%d")
        })

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

        overlapping = Booking.objects.filter(
            unit=unit,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        ).exclude(pk=booking.pk)

        if overlapping.exists():
            messages.error(request, "This unit is not available for the selected dates.")
            return redirect(request.path)

        nights = (check_out_date - check_in_date).days
        base_price = nights * unit.price_per_night

        try:
            dog_count = int(dogs or 0)
        except (TypeError, ValueError):
            dog_count = 0

        dog_surcharge = (
            Decimal("20.00")
            if unit.dogs_allowed and dog_count > 0
            else Decimal("0.00")
        )

        total_amount = base_price + dog_surcharge

        booking.check_in_date = check_in_date
        booking.check_out_date = check_out_date
        booking.adults = adults
        booking.children = children
        booking.dogs = dog_count
        booking.nightly_price = unit.price_per_night
        booking.total_nights = nights
        booking.dog_surcharge = dog_surcharge
        booking.total_amount = total_amount
        booking.save()

        return redirect("booking_detail", pk=booking.pk)

    return render(request, "bookings/booking_update.html", {
        "booking": booking,
        "unit": unit,
        "booked_ranges": booked_ranges
    })

# Booking Delete Requests
@login_required
def booking_delete_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been cancelled.")
        return redirect("my_bookings")

    return render(request, "bookings/booking_delete.html", {"booking": booking})


# Booking Change Requests
@login_required
def booking_change_request_view(request, pk):
    booking = get_object_or_404(Booking, pk=pk, customer=request.user)

    if request.method == "POST":
        message = request.POST.get("message")

        if not message:
            messages.error(request, "Please describe the change you want to request.")
            return redirect(request.path)

        BookingChangeRequest.objects.create(
            booking=booking,
            customer=request.user,
            message=message,
            status="OPEN"
        )

        messages.success(request, "Your change request has been submitted.")
        return redirect("booking_detail", pk=booking.pk)

    return render(request, "bookings/booking_change_request.html", {"booking": booking})


# Admin Dashboard
@login_required
def admin_bookings_list_view(request):
    if not request.user.is_staff:
        return render(request, "403.html")

    bookings = Booking.objects.all().order_by("check_in_date")
    return render(request, "admin/admin_bookings_list.html", {"bookings": bookings})


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
    return render(request, "admin/admin_customer_detail.html", {
        "customer": customer,
        "bookings": bookings,
    })

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

