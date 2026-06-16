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
def book_consultation(request, doctor_id):

    # support booking by doctor id or by service slug
    doctor = None
    service = None

    # doctor_id may be an int (from doctor booking) or a slug string passed via URL name 'book_service'
    try:
        # if doctor_id is int (normal case), fetch doctor
        doctor = get_object_or_404(Doctor, id=doctor_id)
    except Exception:
        # otherwise try to find service by slug
        service = get_object_or_404(Service, slug=doctor_id)

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