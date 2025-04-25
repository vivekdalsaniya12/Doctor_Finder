from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Doctor
from .forms import DoctorForm

# Create your views here.


def home(request):
    form = DoctorForm()
    doctors = Doctor.objects.all()
    return render(request, 'doctorapp/home.html', {'form': form, 'doctors': doctors})

def save_doctor_form(request, form, template_name, doctor=None):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            doctors = Doctor.objects.all()
            data['html_doctor_list'] = render_to_string('doctorapp/includes/partial_doctor_list.html', {
                'doctors': doctors
            })
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    if doctor:
        context['doctor'] = doctor
    elif hasattr(form, 'instance'):
        context['doctor'] = form.instance

    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

from django.template.loader import render_to_string

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    else:
        form = DoctorForm()
    return save_doctor_form(request, form, 'doctorapp/includes/partial_doctor_create.html')

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
    else:
        form = DoctorForm(instance=doctor)
    return save_doctor_form(request, form, 'doctorapp/includes/partial_doctor_update.html', doctor=doctor)

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    data = dict()
    if request.method == 'POST':
        doctor.delete()
        data['form_is_valid'] = True
        doctors = Doctor.objects.all()
        data['html_doctor_list'] = render_to_string('doctorapp/includes/partial_doctor_list.html', {
            'doctors': doctors
        })
    else:
        context = {'doctor': doctor}
        data['html_form'] = render_to_string('doctorapp/includes/partial_doctor_delete.html',
                                             context,
                                             request=request)
    return JsonResponse(data)
