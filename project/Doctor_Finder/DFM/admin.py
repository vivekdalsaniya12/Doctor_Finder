from django.contrib import admin
from .models import Doctor,Doctor_info,Patient
from social_django.models import UserSocialAuth

# Register your models here.

#admin.site.register(Doctor)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialty','email','phone','experience')
    list_filter = ('name','specialty','experience')
    search_fields = ('name','specialty','email')
     
admin.site.register(Doctor_info)
admin.site.register(Patient)
admin.site.register(UserSocialAuth)