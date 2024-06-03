from django.contrib import admin
from .models import NormalEmployee, Nurse, Doctor
# Register your models here.

admin.site.register(NormalEmployee)
admin.site.register(Nurse)
admin.site.register(Doctor)
