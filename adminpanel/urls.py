from django.urls import path
from . import views

urlpatterns = [
    # Admin Dashboard
    path("dashboard/", views.admin_dashboard_view, name="admin_dashboard"),
    # Admin Bookings
    path("bookings/", views.admin_booking_list, name="admin_booking_list"),
    path(
        "bookings/<int:booking_id>/",
        views.admin_booking_detail,
        name="admin_booking_detail",
    ),
    path(
        "bookings/<int:booking_id>/status/",
        views.admin_booking_status_update,
        name="admin_booking_status_update",
    ),
    path(
        "bookings/<int:booking_id>/delete/",
        views.admin_booking_delete,
        name="admin_booking_delete",
    ),
    path(
        "change-request/<int:request_id>/action/",
        views.admin_change_request_action,
        name="admin_change_request_action",
    ),

    # Admin Units
    path("units/", views.admin_units_list, name="admin_unit_list"),
    path(
        "units/<int:unit_id>/",
        views.admin_unit_detail,
        name="admin_unit_detail",
    ),
    #Admin Unit Availability
    path(
    "units/<int:unit_id>/availability/",
    views.admin_unit_availability,
    name="admin_unit_availability",
    ),

    # Admin Customers
    path("customers/", views.admin_customers_list, name="admin_customers_list"),
    path(
        "customers/<int:customer_id>/",
        views.admin_customer_detail,
        name="admin_customer_detail",
    ),
    path(
        "customers/<int:customer_id>/modify/",
        views.admin_modify_customer,
        name="admin_modify_customer",
    ),
]
