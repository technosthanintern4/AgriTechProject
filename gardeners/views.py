from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.contrib.auth.decorators import login_required

from .models import (
    Gardener,
    GardenerBooking
)

from .forms import GardenerBookingForm


def gardener_list(request):

    gardeners = Gardener.objects.filter(
        available=True
    )

    return render(
        request,
        'gardeners/list.html',
        {
            'gardeners': gardeners
        }
    )


@login_required
def book_gardener(request, gardener_id):

    gardener = get_object_or_404(
        Gardener,
        id=gardener_id
    )

    if request.method == 'POST':

        form = GardenerBookingForm(
            request.POST
        )

        if form.is_valid():

            booking = form.save(
                commit=False
            )

            booking.user = request.user
            booking.gardener = gardener

            booking.save()

            return redirect(
                'gardener_booking_success'
            )

    else:

        form = GardenerBookingForm()

    return render(
        request,
        'gardeners/book.html',
        {
            'gardener': gardener,
            'form': form
        }
    )


def gardener_booking_success(request):

    return render(
        request,
        'gardeners/success.html'
    )