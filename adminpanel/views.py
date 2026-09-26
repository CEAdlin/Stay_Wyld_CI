from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from decimal import Decimal
from bookings.models import Booking, Unit, UnitGalleryImage, UnitBlockedDate, BookingChangeRequest
from accounts.models import CustomerProfile
import json
from django.db import transaction


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
            booking.save(update_fields=["status"])
            messages.success(request, "Booking status updated.")

    return redirect("admin_booking_list")


@login_required
def admin_booking_delete(request, booking_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Staff access required.")

    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking deleted.")

    return redirect("admin_booking_list")


@login_required
def admin_units_list(request):
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

    return render(request, "admin/admin_units_list.html", {"units": units})


@login_required
def admin_unit_detail(request, unit_id):
    if not request.user.is_staff:
        return redirect("index")

    unit = get_object_or_404(Unit, id=unit_id)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "save_unit":
            unit.name = request.POST.get("name", "").strip()
            unit.short_description = request.POST.get(
                "short_description", ""
            ).strip()
            unit.description = request.POST.get("description", "").strip()
            unit.max_adults = request.POST.get("max_adults", 1)
            unit.max_children = request.POST.get("max_children", 0)
            unit.price_per_night = request.POST.get("price_per_night", 0)
            unit.dog_surcharge = request.POST.get("dog_surcharge", 0)
            unit.dog_charge_type = request.POST.get(
                "dog_charge_type",
                "PER_DOG_PER_STAY",
            )
            unit.dogs_allowed = "dogs_allowed" in request.POST
            unit.active = "active" in request.POST

            if request.FILES.get("main_image"):
                unit.main_image = request.FILES["main_image"]

            if request.POST.get("delete_main_image") and unit.main_image:
                unit.main_image.delete(save=False)
                unit.main_image = None

            unit.save()

            for image in request.FILES.getlist("gallery_images"):
                UnitGalleryImage.objects.create(
                    unit=unit,
                    image=image,
                )

            messages.success(request, "Unit updated successfully.")

        elif action == "delete_gallery_image":
            image = get_object_or_404(
                UnitGalleryImage,
                id=request.POST.get("image_id"),
                unit=unit,
            )
            image.image.delete(save=False)
            image.delete()
            messages.success(request, "Gallery image deleted.")

        elif action in {"block_dates", "unblock_dates"}:
            try:
                selected_dates = [
                    date.fromisoformat(value)
                    for value in json.loads(request.POST.get("dates", "[]"))
                ]
            except (TypeError, ValueError, json.JSONDecodeError):
                selected_dates = []

            if selected_dates:
                if action == "block_dates":
                    for selected_date in selected_dates:
                        UnitBlockedDate.objects.get_or_create(
                            unit=unit,
                            date=selected_date,
                        )
                    messages.success(
                        request,
                        "Selected dates marked unavailable.",
                    )
                else:
                    UnitBlockedDate.objects.filter(
                        unit=unit,
                        date__in=selected_dates,
                    ).delete()
                    messages.success(request, "Selected dates made available.")

        return redirect("admin_unit_detail", unit_id=unit.id)

    return render(
        request,
        "admin/admin_unit_detail.html",
        {
            "unit": unit,
            "gallery_images": unit.gallery_images.all(),
            "blocked_dates": unit.blocked_dates.all(),
        },
    )

@login_required
def admin_unit_availability(request, unit_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("Staff access required.")

    unit = get_object_or_404(Unit, id=unit_id)
    events = []

    for blocked_date in unit.blocked_dates.all():
        events.append({
            "id": f"blocked-{blocked_date.id}",
            "title": "Unavailable",
            "start": blocked_date.date.isoformat(),
            "allDay": True,
            "className": "admin-calendar-blocked",
            "extendedProps": {
                "type": "blocked",
            },
        })

    bookings = Booking.objects.filter(
        unit=unit,
    ).exclude(status="CANCELLED")

    for booking in bookings:
        current_date = booking.check_in_date

        while current_date < booking.check_out_date:
            events.append({
                "id": (
                    f"booking-{booking.id}-"
                    f"{current_date.isoformat()}"
                ),
                "title": "Booked",
                "start": current_date.isoformat(),
                "allDay": True,
                "className": "admin-calendar-booked",
                "extendedProps": {
                    "type": "booking",
                    "booking_id": booking.id,
                },
            })

            current_date += timedelta(days=1)

    return JsonResponse(events, safe=False)

@login_required
def admin_modify_unit(request, unit_id):
    if not request.user.is_staff:
        return redirect("index")
    unit = get_object_or_404(Unit, id=unit_id)
    messages.info(request, "Modify unit page not yet implemented.")
    return redirect("admin_unit_detail", unit_id=unit_id)

@login_required
def admin_customers_list(request):
    if not request.user.is_superuser:
        return redirect("index")

    today = date.today()
    customers = list(User.objects.filter(is_superuser=False).order_by("username"))  

    for customer in customers:
        profile = CustomerProfile.objects.filter(user=customer).first()
        bookings = Booking.objects.filter(customer=customer)

        customer.customer_name = (
            profile.full_name if profile else customer.get_full_name() or customer.username
        )
        customer.email_address = customer.email
        customer.phone_number = (
            profile.phone_number if profile else "Not provided"
        )
        customer.total_bookings = bookings.count()
        customer.has_active_booking = (
            bookings.filter(
                check_in_date__lte=today,
                check_out_date__gte=today,
            )
            .exclude(status="CANCELLED")
            .exists()
        )

    sort_by = request.GET.get("sort", "name")
    search_query = request.GET.get("search", "").strip()

    if search_query:
        search_value = search_query.casefold()
        customers = [
            customer
            for customer in customers
            if search_value in customer.customer_name.casefold()
        ]

    if sort_by == "active":
        customers.sort(
            key=lambda customer: (
                not customer.has_active_booking,
                customer.username.lower(),
            )
        )
    else:
        customers.sort(key=lambda customer: customer.username.lower())

    return render(
        request,
        "admin/admin_customers_list.html",
        {
            "customers": customers,
            "sort_by": sort_by,
            "search_query": search_query,
        },
    )


@login_required
def admin_customer_detail(request, customer_id):
    if not request.user.is_superuser:
        return redirect("index")

    customer = get_object_or_404(User, id=customer_id)
    profile = CustomerProfile.objects.filter(user=customer).first()

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()

        if not full_name or not email or not phone:
            messages.error(request, "Please complete all required fields.")
        elif len(address) < 20:
            messages.error(
                request,
                "Address must be at least 20 characters.",
            )
        elif User.objects.filter(
            username=email
        ).exclude(pk=customer.pk).exists():
            messages.error(request, "That email address is already in use.")
        else:
            customer.email = email
            customer.username = email
            customer.save(update_fields=["email", "username"])

            if profile:
                profile.full_name = full_name
                profile.phone_number = phone
                profile.address = address
                profile.save()
            else:
                CustomerProfile.objects.create(
                    user=customer,
                    full_name=full_name,
                    phone_number=phone,
                    address=address,
                )

            messages.success(request, "Customer record updated successfully.")
            return redirect(
                "admin_customer_detail",
                customer_id=customer.id,
            )

    bookings = (
        Booking.objects
        .filter(customer=customer)
        .select_related("unit")
        .order_by("-check_in_date")
    )

    return render(
        request,
        "admin/admin_customer_detail.html",
        {
            "customer": customer,
            "profile": profile,
            "bookings": bookings,
        },
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
        .order_by("check_in_date")
    )

    status_filter = request.GET.get("status") or "active"
    unit_filter = request.GET.get("unit")
    booking_id_filter = request.GET.get("booking_id", "").strip()
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    today = date.today()

    if status_filter == "past":
        bookings = bookings.filter(check_out_date__lt=today)
    elif status_filter == "current":
        bookings = bookings.filter(
            check_in_date__lte=today,
            check_out_date__gte=today,
        )
    elif status_filter == "upcoming":
        bookings = bookings.filter(check_in_date__gt=today)
    else:
        bookings = bookings.filter(check_out_date__gte=today)

    if date_from:
        bookings = bookings.filter(check_in_date__gte=date_from)

    if date_to:
        bookings = bookings.filter(check_out_date__lte=date_to)

    if unit_filter:
        bookings = bookings.filter(unit_id=unit_filter)

    if booking_id_filter:
        if booking_id_filter.isdigit():
            bookings = bookings.filter(id=int(booking_id_filter))
        else:
            bookings = bookings.none()

    for booking in bookings:
        booking.latest_request = (
            booking.change_requests.all().order_by("-created_at").first()
        )

    return render(
        request,
        "admin/admin_booking_list.html",
        {
            "bookings": bookings,
            "status_choices": Booking.STATUS_CHOICES,
            "status_filter": status_filter,
            "unit_filter": unit_filter,
            "booking_id_filter": booking_id_filter,
            "units": Unit.objects.order_by("name"),
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
        return redirect("admin_booking_list")

    change_requests = booking.change_requests.order_by("-created_at")

    return render(
        request,
        "admin/admin_booking_detail.html",
        {
            "booking": booking,
            "status_choices": Booking.STATUS_CHOICES,
            "change_requests": change_requests,
        },
    )


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
                    booking.total_nights * booking.nightly_price + booking.dog_surcharge
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
