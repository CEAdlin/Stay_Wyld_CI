from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bookings.models import Booking
from bookings.models import Unit
from django.contrib.auth.models import User

from datetime import date


@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return redirect("index")
    return render(request, "admin/admin_dashboard.html")


@login_required
def admin_unit_list(request):
    units = Unit.objects.all()
    today = date.today()

    for unit in units:
        todays_bookings = Booking.objects.filter(
            unit=unit,
            check_in_date__lte=today,
            check_out_date__gte=today
        )

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
    unit = get_object_or_404(Unit, id=unit_id)

    today = date.today()
    todays_bookings = Booking.objects.filter(
        unit=unit,
        check_in_date__lte=today,
        check_out_date__gte=today
    )

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
    unit = get_object_or_404(Unit, id=unit_id)
    messages.info(request, "Modify unit page not yet implemented.")
    return redirect("admin_unit_detail", unit_id=unit_id)


@login_required
def admin_customers_list(request):
    customers = User.objects.all().order_by("username")
    return render(request, "admin/admin_customers_list.html", {"customers": customers})


@login_required
def admin_customer_detail(request, customer_id):
    customer = get_object_or_404(User, id=customer_id)
    bookings = Booking.objects.filter(customer=customer)

    return render(request, "admin/admin_customer_detail.html", {
        "customer": customer,
        "bookings": bookings
    })


@login_required
def admin_modify_customer(request, customer_id):
    customer = get_object_or_404(User, id=customer_id)
    messages.info(request, "Modify customer page not yet implemented.")
    return redirect("admin_customer_detail", customer_id=customer_id)


@login_required
def admin_booking_list(request):
    bookings = Booking.objects.all().order_by("-check_in_date")

    status_filter = request.GET.get("status")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")

    today = date.today()

    if status_filter == "past":
        bookings = bookings.filter(check_out_date__lt=today)
    elif status_filter == "current":
        bookings = bookings.filter(
            check_in_date__lte=today,
            check_out_date__gte=today
        )
    elif status_filter == "upcoming":
        bookings = bookings.filter(check_in_date__gt=today)

    if date_from:
        bookings = bookings.filter(check_in_date__gte=date_from)

    if date_to:
        bookings = bookings.filter(check_out_date__lte=date_to)

    return render(request, "admin/admin_booking_list.html", {"bookings": bookings})


@login_required
def admin_booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, "admin/admin_booking_detail.html", {"booking": booking})


@login_required
def admin_modify_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    messages.info(request, "Modify booking page not yet implemented.")
    return redirect("admin_booking_detail", booking_id=booking_id)
