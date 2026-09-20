from django.contrib import admin
from .models import Unit, UnitGalleryImage, Booking

#Drag and drop ordering for gallery images in the admin interface
from adminsortable2.admin import SortableInlineAdminMixin

class UnitGalleryImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = UnitGalleryImage
    extra = 1
    fields = ("image", "position")


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "active", "max_guests", "base_price_per_night")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [UnitGalleryImageInline]


@admin.register(UnitGalleryImage)
class UnitGalleryImageAdmin(admin.ModelAdmin):
    list_display = ("unit", "image")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("unit", "customer", "check_in_date", "check_out_date", "total_price", "status")
