from django import forms
from .models import Doctor_info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DoctorProfile(forms.ModelForm):
    class Meta:
        model = Doctor_info
        fields = ['name','email','phone','address','specialty','experience','hospital','city']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'specialty' : forms.TextInput(attrs={'class':'form-control'}),
            'experience' : forms.NumberInput(attrs={'class':'form-control'}),
            'hospital' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']