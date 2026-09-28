from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Booking, BookingChangeRequest, Unit, UnitBlockedDate
from .validation import calculate_dog_surcharge


class BookingAvailabilityTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(
            username="booking-admin",
            password="test-password",
            is_staff=True,
        )
        self.unit = Unit.objects.create(
            name="Test Unit",
            slug="test-unit",
            price_per_night="100.00",
        )
        self.client.force_login(self.staff_user)

    def booking_data(self, check_in, check_out):
        return {
            "check_in": check_in.isoformat(),
            "check_out": check_out.isoformat(),
            "customer_name": "Test Customer",
            "customer_email": "test@example.com",
            "customer_phone": "01234567890",
            "adults": "1",
            "children": "0",
            "dogs": "0",
        }

    def create_booking(self, check_in, check_out):
        return Booking.objects.create(
            unit=self.unit,
            customer_name="Existing Customer",
            customer_email="existing@example.com",
            customer_phone="01234567890",
            check_in_date=check_in,
            check_out_date=check_out,
            nightly_price="100.00",
            total_nights=(check_out - check_in).days,
            total_amount="200.00",
            status="CONFIRMED",
        )

    def test_check_in_is_allowed_on_existing_checkout_date(self):
        existing_check_in = date(2026, 10, 10)
        existing_check_out = date(2026, 10, 12)
        self.create_booking(existing_check_in, existing_check_out)

        new_check_out = existing_check_out + timedelta(days=2)
        response = self.client.post(
            reverse("booking_create", args=[self.unit.slug]),
            self.booking_data(existing_check_out, new_check_out),
        )

        self.assertRedirects(response, reverse("admin_booking_list"))
        self.assertTrue(
            Booking.objects.filter(
                unit=self.unit,
                check_in_date=existing_check_out,
                check_out_date=new_check_out,
            ).exists()
        )

    def test_blocked_night_cannot_be_booked(self):
        blocked_date = date(2026, 10, 11)
        UnitBlockedDate.objects.create(unit=self.unit, date=blocked_date)

        response = self.client.post(
            reverse("booking_create", args=[self.unit.slug]),
            self.booking_data(
                date(2026, 10, 10),
                date(2026, 10, 12),
            ),
        )

        self.assertRedirects(
            response,
            reverse("booking_create", args=[self.unit.slug]),
        )
        self.assertFalse(Booking.objects.filter(unit=self.unit).exists())

    @override_settings(DEBUG=False)
    def test_invalid_url_returns_custom_404_page(self):
        response = self.client.get("/this-page-does-not-exist/")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Page Not Found", status_code=404)

    def test_per_dog_surcharge_uses_unit_configuration(self):
        self.unit.dogs_allowed = True
        self.unit.dog_surcharge = "50.00"
        self.unit.dog_charge_type = "PER_DOG_PER_STAY"
        self.unit.save()

        check_in = date(2026, 10, 10)
        check_out = date(2026, 10, 12)
        response = self.client.post(
            reverse("booking_create", args=[self.unit.slug]),
            {**self.booking_data(check_in, check_out), "dogs": "2"},
        )

        self.assertRedirects(response, reverse("admin_booking_list"))
        booking = Booking.objects.get(unit=self.unit)
        self.assertEqual(booking.dog_surcharge, Decimal("100.00"))
        self.assertEqual(booking.total_amount, Decimal("300.00"))

    def test_per_stay_surcharge_uses_unit_configuration(self):
        self.unit.dogs_allowed = True
        self.unit.dog_surcharge = "50.00"
        self.unit.dog_charge_type = "PER_STAY"
        self.unit.save()

        check_in = date(2026, 10, 10)
        check_out = date(2026, 10, 12)
        response = self.client.post(
            reverse("booking_create", args=[self.unit.slug]),
            {**self.booking_data(check_in, check_out), "dogs": "2"},
        )

        self.assertRedirects(response, reverse("admin_booking_list"))
        booking = Booking.objects.get(unit=self.unit)
        self.assertEqual(booking.dog_surcharge, Decimal("50.00"))
        self.assertEqual(booking.total_amount, Decimal("250.00"))

    def test_customer_can_cancel_booking_directly(self):
        booking = Booking.objects.create(
            unit=self.unit,
            customer=self.staff_user,
            customer_name="Existing Customer",
            customer_email="existing@example.com",
            customer_phone="01234567890",
            check_in_date=date(2026, 10, 10),
            check_out_date=date(2026, 10, 12),
            nightly_price="100.00",
            total_nights=2,
            total_amount="200.00",
            status="CONFIRMED",
        )
        BookingChangeRequest.objects.create(
            booking=booking,
            customer=self.staff_user,
            request_type="CANCEL",
            message="Old cancellation request",
            status="OPEN",
        )

        response = self.client.post(
            reverse("booking_delete", args=[booking.pk])
        )

        self.assertRedirects(
            response,
            f"{reverse('booking_detail', args=[booking.pk])}?cancelled=1",
        )
        booking.refresh_from_db()
        self.assertEqual(booking.status, "CANCELLED")
        self.assertFalse(
            BookingChangeRequest.objects.filter(
                booking=booking,
                status="OPEN",
            ).exists()
        )
