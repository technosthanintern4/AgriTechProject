from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from doctors.models import Doctor
from .forms import ConsultationForm
from services.models import Service


@login_required
def book_consultation(request, doctor_id=None, service_slug=None):

    # support booking by doctor id (doctor_id) or by service slug (service_slug)
    doctor = None
    service = None

    if doctor_id:
        # doctor_id route uses an integer id
        doctor = get_object_or_404(Doctor, id=doctor_id)
    elif service_slug:
        service = get_object_or_404(Service, slug=service_slug)

    if request.method == 'POST':

        form = ConsultationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            consultation = form.save(commit=False)

            consultation.user = request.user
            if doctor:
                consultation.doctor = doctor
            if service:
                consultation.service = service

            consultation.save()

            return redirect(
                'consultation_success'
            )

    else:

        form = ConsultationForm()

    return render(request, 'consultations/book.html', {
        'doctor': doctor,
        'service': service,
        'form': form
    })


@login_required
def consultation_success(request):

    return render(
        request,
        'consultations/success.html'
    )