from django.urls import path
from . import views

urlpatterns = [

    # Homepage
    path("", views.index_view, name="index"),

    # Units
    path("units/", views.units_list_view, name="units_list"),
    path("units/<slug:unit_slug>/", views.unit_detail_view, name="unit_detail"),

    # Booking flow
    path("units/<slug:unit_slug>/book/", views.booking_create_view, name="booking_create"),
    path("units/<slug:unit_slug>/calendar/", views.availability_calendar_view, name="availability_calendar"),

    # Customer dashboard
    path("my-bookings/", views.my_bookings_view, name="my_bookings"),
    path("booking/<int:pk>/", views.booking_detail_view, name="booking_detail"),
    path("booking/<int:pk>/update/", views.booking_update_view, name="booking_update"),
    path("booking/<int:pk>/delete/", views.booking_delete, name="booking_delete"),

    # Admin dashboard (custom)
    path("manage/bookings/", views.admin_bookings_list_view, name="admin_bookings_list"),
    path("manage/bookings/<int:pk>/", views.admin_booking_detail_view, name="admin_booking_detail"),

    path("manage/units/", views.admin_units_list_view, name="admin_units_list"),
    path("manage/units/<slug:unit_slug>/", views.admin_unit_detail_view, name="admin_unit_detail"),

    path("manage/customers/", views.admin_customers_list_view, name="admin_customers_list"),
    path("manage/customers/<int:user_id>/", views.admin_customer_detail_view, name="admin_customer_detail"),
]
