from datetime import datetime, time

from django.core.management.base import BaseCommand
from django.utils import timezone

from bookings.models import Booking


class Command(BaseCommand):
    help = "Marks bookings as completed after 11:00 on their checkout date."

    def handle(self, *args, **options):
        now = timezone.localtime()
        checkout_cutoff = datetime.combine(
            now.date(),
            time(11, 0),
            tzinfo=now.tzinfo,
        )

        if now < checkout_cutoff:
            self.stdout.write("Checkout cutoff has not been reached.")
            return

        bookings = Booking.objects.filter(
            check_out_date__lte=now.date(),
        ).exclude(
            status__in=["CANCELLED", "COMPLETED"],
        )

        updated = bookings.update(status="COMPLETED")

        self.stdout.write(
            self.style.SUCCESS(
                f"{updated} booking(s) marked as completed."
            )
        )