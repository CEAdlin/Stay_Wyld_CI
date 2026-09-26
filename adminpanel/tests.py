import json
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomerProfile
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

	def test_unit_filter_shows_only_selected_unit_bookings(self):
		other_unit = Unit.objects.create(
			name="Other Unit",
			slug="other-unit",
			price_per_night="120.00",
		)
		today = date.today()
		selected_booking = self.create_booking(
			today,
			today + timedelta(days=2),
		)
		other_booking = Booking.objects.create(
			unit=other_unit,
			customer_name="Other Customer",
			customer_email="other@example.com",
			customer_phone="01234567890",
			check_in_date=today,
			check_out_date=today + timedelta(days=2),
			nightly_price="120.00",
			total_nights=2,
			total_amount="240.00",
		)

		response = self.client.get(
			reverse("admin_booking_list"),
			{"unit": self.unit.id},
		)

		self.assertEqual(
			list(response.context["bookings"]),
			[selected_booking],
		)
		self.assertNotIn(other_booking, response.context["bookings"])


class AdminCustomerListTests(TestCase):
	def setUp(self):
		self.admin_user = User.objects.create_user(
			username="customer-list-admin",
			password="test-password",
			is_superuser=True,
			is_staff=True,
		)
		self.client.force_login(self.admin_user)

	def create_customer(self, username, full_name):
		customer = User.objects.create_user(
			username=username,
			password="test-password",
		)
		CustomerProfile.objects.create(
			user=customer,
			full_name=full_name,
			address="123 Woodland Lane, Codsall, Staffordshire",
			phone_number="01234567890",
		)
		return customer

	def test_customer_name_search_is_case_insensitive_and_partial(self):
		sophie = self.create_customer("sophie@example.com", "Sophie Jones")
		sam = self.create_customer("sam@example.com", "Samuel Smith")
		self.create_customer("alex@example.com", "Alex Brown")

		response = self.client.get(
			reverse("admin_customers_list"),
			{"search": "S"},
		)

		self.assertEqual(
			{customer.id for customer in response.context["customers"]},
			{sophie.id, sam.id},
		)

		response = self.client.get(
			reverse("admin_customers_list"),
			{"search": "sophie"},
		)

		self.assertEqual(
			[customer.id for customer in response.context["customers"]],
			[sophie.id],
		)
