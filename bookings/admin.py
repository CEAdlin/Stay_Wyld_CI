from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Unit, UnitGalleryImage, Booking


# Drag‑and‑drop gallery image ordering
class UnitGalleryImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = UnitGalleryImage
    extra = 1
    fields = ("image", "position")


# Unit admin must inherit from SortableAdminBase
@admin.register(Unit)
class UnitAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("name", "slug", "active", "max_guests", "price_per_night", "dogs_allowed")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [UnitGalleryImageInline]


@admin.register(UnitGalleryImage)
class UnitGalleryImageAdmin(admin.ModelAdmin):
    list_display = ("unit", "image")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("unit", "customer", "check_in_date", "check_out_date", "total_amount", "status")
