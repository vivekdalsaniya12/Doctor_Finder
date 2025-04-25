from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import DoctorProfile,SignupForm, UpdateProfileForm
from .models import Doctor,Doctor_info,Patient
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from paytmchecksum import PaytmChecksum # type: ignore


# Create your views here.

def home(request):
    return render(request,'DFM/home.html')

def  doctor_profile(request):
    if request.method=='POST':
        fm = DoctorProfile(request.POST)
        if fm.is_valid():
            nn = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            po = fm.cleaned_data['phone']
            ad = fm.cleaned_data['address']
            sp = fm.cleaned_data['specialty']
            ex = fm.cleaned_data['experience']
            ho = fm.cleaned_data['hospital']
            ci = fm.cleaned_data['city']
            reg = Doctor_info(name=nn,email=em,phone=po,address=ad,specialty=sp,experience=ex,hospital=ho,city=ci)
            reg.save()
            fm = DoctorProfile()
    else:
        fm = DoctorProfile()
    return render(request,'DFM/profile.html',{'form':fm})

# def registration(request):
#     return render(request,'DFM/register.html')

def doctor_list(request):
    doctor = Doctor_info.objects.all()
    return render(request,'DFM/doctor_list.html',{'doctors':doctor})

def delete(request, id):
    if request.method =='POST':
        pi = Doctor_info.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/doctor_list')
    
def update(request,id):
    if request.method=='POST':
        pi = Doctor_info.objects.get(pk=id)
        fm = DoctorProfile(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Doctor_info.objects.get(pk=id)
        fm = DoctorProfile(instance=pi)
    
    return render(request,'DFM/update.html',{'form':fm}) 

def register(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration successful.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'DFM/signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        uname = request.POST['username']
        pw = request.POST['password']
        user = authenticate(username=uname,password=pw)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return render(request, 'DFM/login.html', {'error': 'Invalid username or password'})
    return render(request,'DFM/login.html')

def profile(request):
    return render(request,'DFM/profile1.html')

def update_profile(request):
    if request.method=='POST':
        form = UpdateProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request,'DFM/update_profile.html',{'form':form})

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password Change Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'DFM/change_password.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def register_patient(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        patient = Patient.objects.create(name=name, email=email, phone=phone)
        request.session['patient_id'] = patient.id
        return redirect('pay')
    return render(request, 'DFM/register.html')


def initiate_payment(request):
    patient_id = request.session.get('patient_id')
    patient = Patient.objects.get(id=patient_id)

    order_id = f'ORDER{patient_id}XYZ'
    amount = '100'  # Fixed amount for demo

    param_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'ORDER_ID': order_id,
        'TXN_AMOUNT': amount,
        'CUST_ID': str(patient_id),
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
    }

    checksum = PaytmChecksum.generateSignature(param_dict, settings.PAYTM_MERCHANT_KEY)
    param_dict['CHECKSUMHASH'] = checksum

    return render(request, 'DFM/payment.html', {'param_dict': param_dict})

@csrf_exempt
def payment_response(request):
    response_dict = dict(request.POST)
    paytm_params = {k: v[0] for k, v in response_dict.items()}
    checksum = paytm_params.pop('CHECKSUMHASH', '')

    is_valid_checksum = PaytmChecksum.verifySignature(paytm_params, settings.PAYTM_MERCHANT_KEY, checksum)

    if is_valid_checksum and paytm_params['RESPCODE'] == '01':
        patient = Patient.objects.get(id=paytm_params['CUST_ID'])
        patient.payment_status = 'Success'
        patient.save()
        return HttpResponse("Payment Successful")
    else:
        return HttpResponse(f"Payment Failed: {paytm_params.get('RESPMSG', '')}")