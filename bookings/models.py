# bookings/models.py

from django.db import models
from django.contrib.auth.models import User

# UNIT MODEL

class Unit(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    # Main content
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    # Images
    main_image = models.ImageField(upload_to="unit_main/", blank=True, null=True)

    # Capacity & pricing
    max_adults = models.PositiveIntegerField(default=2)
    max_children = models.PositiveIntegerField(default=2)

    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    dog_surcharge = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    # Flags
    dogs_allowed = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# GALLERY MODEL

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

    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)

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
        # Prefer admin-entered name if present
        if self.customer_name:
            return f"{self.customer_name} - {self.unit.name} ({self.check_in_date})"
        return f"{self.customer.username} - {self.unit.name} ({self.check_in_date})"


# BOOKING CHANGE REQUEST

class BookingChangeRequest(models.Model):
    REQUEST_TYPES = [
        ("MODIFY", "Modification"),
        ("CANCEL", "Cancellation"),
    ]

    STATUS_CHOICES = [
    ("OPEN", "Open"),
    ("APPROVED", "Accepted"),
    ("REJECTED", "Declined"),
]

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="change_requests",
    )
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(
        max_length=10,
        choices=REQUEST_TYPES,
        default="MODIFY",
    )
    message = models.TextField()

    requested_check_in = models.DateField(null=True, blank=True)
    requested_check_out = models.DateField(null=True, blank=True)
    requested_adults = models.PositiveIntegerField(null=True, blank=True)
    requested_children = models.PositiveIntegerField(null=True, blank=True)
    requested_dogs = models.PositiveIntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change Request for Booking {self.booking.id}"