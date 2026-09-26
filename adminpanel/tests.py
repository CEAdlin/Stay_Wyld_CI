import json
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from bookings.models import Booking, Unit, UnitBlockedDate


class AdminUnitAvailabilityTests(TestCase):
	def setUp(self):
		self.staff_user = User.objects.create_user(
			username="admin",
			password="test-password",
			is_staff=True,
		)
		self.unit = Unit.objects.create(
			name="Test Unit",
			slug="test-unit",
			price_per_night="100.00",
		)
		self.client.force_login(self.staff_user)

	def test_block_and_unblock_selected_dates(self):
		selected_dates = ["2026-10-10", "2026-10-11"]
		url = reverse("admin_unit_detail", args=[self.unit.id])

		response = self.client.post(
			url,
			{
				"action": "block_dates",
				"dates": json.dumps(selected_dates),
			},
		)

		self.assertRedirects(response, url)
		self.assertEqual(
			UnitBlockedDate.objects.filter(unit=self.unit).count(),
			2,
		)

		response = self.client.post(
			url,
			{
				"action": "unblock_dates",
				"dates": json.dumps([selected_dates[0]]),
			},
		)

		self.assertRedirects(response, url)
		self.assertFalse(
			UnitBlockedDate.objects.filter(
				unit=self.unit,
				date=selected_dates[0],
			).exists()
		)
		self.assertTrue(
			UnitBlockedDate.objects.filter(
				unit=self.unit,
				date=selected_dates[1],
			).exists()
		)


class AdminBookingListTests(TestCase):
	def setUp(self):
		self.staff_user = User.objects.create_user(
			username="booking-list-admin",
			password="test-password",
			is_staff=True,
		)
		self.unit = Unit.objects.create(
			name="Test Unit",
			slug="booking-list-unit",
			price_per_night="100.00",
		)
		self.client.force_login(self.staff_user)

	def create_booking(self, check_in, check_out):
		return Booking.objects.create(
			unit=self.unit,
			customer_name="Test Customer",
			customer_email="test@example.com",
			customer_phone="01234567890",
			check_in_date=check_in,
			check_out_date=check_out,
			nightly_price="100.00",
			total_nights=(check_out - check_in).days,
			total_amount="200.00",
		)

	def test_default_list_shows_active_bookings_earliest_first(self):
		today = date.today()
		past = self.create_booking(today - timedelta(days=5), today - timedelta(days=2))
		earliest_active = self.create_booking(today, today + timedelta(days=2))
		latest_active = self.create_booking(today + timedelta(days=4), today + timedelta(days=6))

		response = self.client.get(reverse("admin_booking_list"))

		self.assertEqual(
			list(response.context["bookings"]),
			[earliest_active, latest_active],
		)
		self.assertNotIn(past, response.context["bookings"])

	def test_past_filter_shows_past_bookings_earliest_first(self):
		today = date.today()
		latest_past = self.create_booking(today - timedelta(days=5), today - timedelta(days=2))
		earliest_past = self.create_booking(today - timedelta(days=10), today - timedelta(days=7))

		response = self.client.get(
			reverse("admin_booking_list"),
			{"status": "past"},
		)

		self.assertEqual(
			list(response.context["bookings"]),
			[earliest_past, latest_past],
		)
