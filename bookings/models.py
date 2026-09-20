# bookings/models.py

from django.db import models
from django.contrib.auth.models import User

# UNIT MODEL

class Unit(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    max_guests = models.PositiveIntegerField(default=2)
    base_price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    dog_friendly = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UnitGalleryImage(models.Model):
    unit = models.ForeignKey(Unit, related_name="gallery_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="unit_gallery/")
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return f"Gallery image for {self.unit.name}"

# BOOKING MODEL

class Booking(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
        ("COMPLETED", "Completed"),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    check_in_date = models.DateField()
    check_out_date = models.DateField()

    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    infants = models.PositiveIntegerField(default=0)
    dogs = models.PositiveIntegerField(default=0)

    dog_surcharge = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    nightly_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_nights = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    special_requests = models.TextField(blank=True)
    agreed_terms = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.username} - {self.unit.name} ({self.check_in_date})"

# BOOKING CHANGE REQUEST

class BookingChangeRequest(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("REVIEWED", "Reviewed"),
        ("RESOLVED", "Resolved"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="OPEN")

    def __str__(self):
        return f"Change Request for Booking {self.booking.id}"
