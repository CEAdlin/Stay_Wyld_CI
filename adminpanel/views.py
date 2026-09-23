from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from datetime import date, datetime
from decimal import Decimal
from bookings.models import Booking, Unit, BookingChangeRequest


@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return redirect("index")
    return render(request, "admin/admin_dashboard.html")


@login_required
def admin_booking_status_update(request, booking_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Staff access required.")

    if request.method == "POST":
        booking = get_object_or_404(Booking, id=booking_id)
        status = request.POST.get("status")

        if status not in dict(Booking.STATUS_CHOICES):
            messages.error(request, "Invalid booking status.")
        else:
            booking.status = status
            booking.save(update_fields=["status", "updated_at"])
            messages.success(request, "Booking status updated.")

    return redirect("admin_booking_list")


@login_required
def admin_unit_list(request):
    if not request.user.is_staff:
        return redirect("index")
    units = Unit.objects.all()
    today = date.today()

    for unit in units:
        todays_bookings = Booking.objects.filter(
            unit=unit, check_in_date__lte=today, check_out_date__gte=today
        ).exclude(status="CANCELLED")

        if todays_bookings.exists():
            booking = todays_bookings.first()

            if booking.check_in_date == today:
                unit.today_status = "Check-in Today"
            elif booking.check_out_date == today:
                unit.today_status = "Check-out Today"
            else:
                unit.today_status = "Occupied"
        else:
            unit.today_status = "Vacant"

    return render(request, "admin/admin_unit_list.html", {"units": units})


@login_required
def admin_unit_detail(request, unit_id):
    if not request.user.is_staff:
        return redirect("index")
    unit = get_object_or_404(Unit, id=unit_id)

    today = date.today()
    todays_bookings = Booking.objects.filter(
        unit=unit, check_in_date__lte=today, check_out_date__gte=today
    ).exclude(status="CANCELLED")

    if todays_bookings.exists():
        booking = todays_bookings.first()

        if booking.check_in_date == today:
            unit.today_status = "Check-in Today"
        elif booking.check_out_date == today:
            unit.today_status = "Check-out Today"
        else:
            unit.today_status = "Occupied"
    else:
        unit.today_status = "Vacant"

    return render(request, "admin/admin_unit_detail.html", {"unit": unit})


@login_required
def admin_modify_unit(request, unit_id):
    if not request.user.is_staff:
        return redirect("index")
    unit = get_object_or_404(Unit, id=unit_id)
    messages.info(request, "Modify unit page not yet implemented.")
    return redirect("admin_unit_detail", unit_id=unit_id)


@login_required
def admin_customers_list(request):
    if not request.user.is_staff:
        return redirect("index")
    customers = User.objects.all().order_by("username")
    return render(request, "admin/admin_customers_list.html", {"customers": customers})


@login_required
def admin_customer_detail(request, customer_id):
    if not request.user.is_staff:
        return redirect("index")
    customer = get_object_or_404(User, id=customer_id)
    bookings = Booking.objects.filter(customer=customer)

    return render(
        request,
        "admin/admin_customer_detail.html",
        {"customer": customer, "bookings": bookings},
    )


@login_required
def admin_modify_customer(request, customer_id):
    if not request.user.is_staff:
        return redirect("index")
    customer = get_object_or_404(User, id=customer_id)
    messages.info(request, "Modify customer page not yet implemented.")
    return redirect("admin_customer_detail", customer_id=customer_id)


@login_required
def admin_booking_list(request):
    if not request.user.is_staff:
        return redirect("index")

    bookings = (
        Booking.objects.prefetch_related("change_requests")
        .all()
        .order_by("-check_in_date")
    )

    status_filter = request.GET.get("status")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    today = date.today()

    if status_filter == "past":
        bookings = bookings.filter(check_out_date__lt=today)
    elif status_filter == "current":
        bookings = bookings.filter(check_in_date__lte=today, check_out_date__gte=today)
    elif status_filter == "upcoming":
        bookings = bookings.filter(check_in_date__gt=today)

    if date_from:
        bookings = bookings.filter(check_in_date__gte=date_from)

    if date_to:
        bookings = bookings.filter(check_out_date__lte=date_to)

    return render(
        request,
        "admin/admin_booking_list.html",
        {
            "bookings": bookings,
            "status_choices": Booking.STATUS_CHOICES,
            "status_filter": status_filter,
        },
    )


@login_required
def admin_booking_detail(request, booking_id):
    if not request.user.is_staff:
        return redirect("index")

    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST" and request.POST.get("action") == "save_booking":
        try:
            check_in = datetime.strptime(request.POST["check_in"], "%Y-%m-%d").date()
            check_out = datetime.strptime(request.POST["check_out"], "%Y-%m-%d").date()

            adults = int(request.POST.get("adults", 1))
            children = int(request.POST.get("children", 0))
            dogs = int(request.POST.get("dogs", 0))
            status = request.POST.get("status")

            if check_out <= check_in:
                raise ValueError("Check-out must be after check-in.")

            if adults < 1 or children < 0 or dogs < 0:
                raise ValueError("Guest values cannot be negative.")

            if status not in dict(Booking.STATUS_CHOICES):
                raise ValueError("Invalid booking status.")

        except (KeyError, TypeError, ValueError):
            messages.error(request, "Please enter valid booking details.")
            return redirect(request.path)

        nights = (check_out - check_in).days
        dog_surcharge = (
            Decimal("20.00")
            if booking.unit.dogs_allowed and dogs > 0
            else Decimal("0.00")
        )
        total_amount = nights * booking.unit.price_per_night + dog_surcharge

        booking.check_in_date = check_in
        booking.check_out_date = check_out
        booking.adults = adults
        booking.children = children
        booking.dogs = dogs
        booking.total_nights = nights
        booking.dog_surcharge = dog_surcharge
        booking.total_amount = total_amount
        booking.status = status
        booking.save()

        messages.success(request, "Booking updated successfully.")
        return redirect(request.path)

    change_requests = booking.change_requests.order_by("-created_at")

    return render(request, "admin/admin_booking_detail.html", {
        "booking": booking,
        "status_choices": Booking.STATUS_CHOICES,
        "change_requests": change_requests,
    })

@login_required
def admin_change_request_action(request, request_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Staff access required.")

    change_request = get_object_or_404(
        BookingChangeRequest,
        id=request_id,
        status="OPEN",
    )

    if request.method == "POST":
        action = request.POST.get("action")
        booking = change_request.booking

        if action == "approve":
            if change_request.request_type == "CANCEL":
                booking.status = "CANCELLED"
                booking.save(update_fields=["status"])

            elif change_request.request_type == "MODIFY":
                booking.check_in_date = change_request.requested_check_in
                booking.check_out_date = change_request.requested_check_out
                booking.adults = change_request.requested_adults
                booking.children = change_request.requested_children
                booking.dogs = change_request.requested_dogs
                booking.total_nights = (
                    booking.check_out_date - booking.check_in_date
                ).days
                booking.dog_surcharge = (
                    Decimal("20.00")
                    if booking.unit.dogs_allowed and booking.dogs > 0
                    else Decimal("0.00")
                )
                booking.total_amount = (
                    booking.total_nights * booking.nightly_price
                    + booking.dog_surcharge
                )
                booking.save()

            change_request.status = "APPROVED"
            change_request.save(update_fields=["status"])
            messages.success(request, "Request approved.")

        elif action == "reject":
            change_request.status = "REJECTED"
            change_request.save(update_fields=["status"])
            messages.success(request, "Request rejected.")

    return redirect(
        "admin_booking_detail",
        booking_id=change_request.booking_id,
    )

