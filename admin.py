from django.contrib import admin
from .models import Bus, Seat, Booking

class SeatInline(admin.TabularInline):
    model = Seat
    extra = 0


class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'destination', 'date', 'time', 'price')
    inlines = [SeatInline]


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'bus', 'seat', 'booking_date')


admin.site.register(Bus, BusAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Seat)