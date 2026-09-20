from django.urls import path
from . import views

urlpatterns = [

    # Admin Dashboard
    path("dashboard/", views.admin_dashboard_view, name="admin_dashboard"),

    # Admin Bookings
    path("bookings/", views.admin_booking_list, name="admin_booking_list"),
    path("bookings/<int:booking_id>/", views.admin_booking_detail, name="admin_booking_detail"),
    path("bookings/<int:booking_id>/modify/", views.admin_modify_booking, name="admin_modify_booking"),

    # Admin Units
    path("units/", views.admin_unit_list, name="admin_unit_list"),
    path("units/<int:unit_id>/", views.admin_unit_detail, name="admin_unit_detail"),
    path("units/<int:unit_id>/modify/", views.admin_modify_unit, name="admin_modify_unit"),

    # Admin Customers
    path("customers/", views.admin_customers_list, name="admin_customers_list"),
    path("customers/<int:customer_id>/", views.admin_customer_detail, name="admin_customer_detail"),
    path("customers/<int:customer_id>/modify/", views.admin_modify_customer, name="admin_modify_customer"),
]
