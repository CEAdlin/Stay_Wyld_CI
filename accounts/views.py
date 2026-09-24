from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import CustomerProfile
from bookings.models import Booking, Unit


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect admins/staff to Admin Dashboard
            if user.is_staff:
                return redirect("admin_dashboard")

            # Redirect normal customers
            return redirect("my_bookings")

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


# Logout View
def logout_view(request):
    logout(request)
    return redirect("index")


# Register View (Customer)
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address", "").strip()

        if len(address) < 20:
            messages.error(
                request,
                "Address is required and must contain at least 20 characters.",
            )
            return render(request, "accounts/register.html")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Email already used?
        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect("register")

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Create profile
        CustomerProfile.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone,
            address=address
        )

        # Auto-login
        login(request, user)
        return redirect("my_bookings")

    return render(request, "accounts/register.html")


# Password Confirmation Modal View 
@login_required
def confirm_sensitive_action(request):
    if request.method != "POST":
        return redirect("index")

    password = request.POST.get("password")
    action_type = request.POST.get("action_type")
    object_id = request.POST.get("object_id")

    # Verify password
    if not request.user.check_password(password):
        messages.error(request, "Incorrect password. Please try again.")
        return redirect(request.META.get("HTTP_REFERER", "index"))

    # Perform action
    if action_type == "delete_booking":
        booking = get_object_or_404(Booking, id=object_id)
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return redirect("admin_booking_list")

    if action_type == "modify_booking":
        return redirect("admin_modify_booking", booking_id=object_id)

    if action_type == "delete_unit":
        unit = get_object_or_404(Unit, id=object_id)
        unit.delete()
        messages.success(request, "Unit deleted successfully.")
        return redirect("admin_unit_list")

    if action_type == "modify_unit":
        return redirect("admin_modify_unit", unit_id=object_id)

    if action_type == "delete_customer":
        customer = get_object_or_404(User, id=object_id)
        customer.delete()
        messages.success(request, "Customer deleted successfully.")
        return redirect("admin_customers_list")

    if action_type == "modify_customer":
        return redirect("admin_modify_customer", customer_id=object_id)

    return redirect("index")
