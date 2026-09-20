from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import CustomerProfile


# -------------------------
# LOGIN VIEW
# -------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("my_bookings")  # or wherever you want them to land
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


# -------------------------
# LOGOUT VIEW
# -------------------------
def logout_view(request):
    logout(request)
    return redirect("index")


# -------------------------
# REGISTER VIEW
# -------------------------
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
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

        # Log user in immediately
        login(request, user)

        return redirect("my_bookings")

    return render(request, "accounts/register.html")
