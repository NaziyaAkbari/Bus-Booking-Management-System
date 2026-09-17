from django.shortcuts import render, redirect
from .models import Bus, Seat, Booking


def dashboard(request):
    buses = Bus.objects.all()
    return render(request, 'booking/dashboard.html', {'buses': buses})


def seat_selection(request, bus_id):
    bus = Bus.objects.get(id=bus_id)
    seats = Seat.objects.filter(bus=bus).order_by('seat_number')

    return render(request, 'booking/seat_selection.html', {
        'bus': bus,
        'seats': seats
    })


def book_seat(request, seat_id):
    seat = Seat.objects.get(id=seat_id)

    if request.method == "POST":
        name = request.POST.get('name')

        if not seat.is_booked:
            Booking.objects.create(
                user_name=name,
                bus=seat.bus,
                seat=seat
            )

            seat.is_booked = True
            seat.save()

            return redirect('booking_success')

    return render(request, 'booking/enter_name.html', {'seat': seat})


def booking_success(request):
    return render(request, 'booking/booking_success.html')


def report(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'booking/report.html', {'bookings': bookings})