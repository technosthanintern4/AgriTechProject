from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from doctors.models import Doctor
from .forms import ConsultationForm


@login_required
def book_consultation(request, doctor_id):

    doctor = get_object_or_404(
        Doctor,
        id=doctor_id
    )

    if request.method == 'POST':

        form = ConsultationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            consultation = form.save(
                commit=False
            )

            consultation.user = request.user
            consultation.doctor = doctor

            consultation.save()

            return redirect(
                'consultation_success'
            )

    else:

        form = ConsultationForm()

    return render(
        request,
        'consultations/book.html',
        {
            'doctor': doctor,
            'form': form
        }
    )


@login_required
def consultation_success(request):

    return render(
        request,
        'consultations/success.html'
    )