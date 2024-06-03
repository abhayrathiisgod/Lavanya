from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from doctors.models import Doctor, NormalEmployee


class Patient(models.Model):

    # Personal Information
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(help_text='AD DOB',blank=True, null=True)
    date_of_birth_ne = models.DateField(help_text='BS DOB',blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    blood_group = models.CharField(max_length=3, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')])
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    facebookId = models.CharField(max_length=255, blank=True, null=True)
    InstagramId =models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    patient_complaint = CKEditor5Field('Patient Complaint', config_name='extends', blank=True, null=True)
    medical_history =CKEditor5Field('Medical History', config_name='extends', blank=True, null=True)
    Investigation = CKEditor5Field('Investigation', config_name='extends', blank=True, null=True)
    diagnosis = CKEditor5Field('Diagnosis', config_name='extends', blank=True, null=True)
    Treatement = CKEditor5Field('Treatment', config_name='extends', blank=True, null=True)
    
    registered_by = models.ForeignKey(NormalEmployee, on_delete=models.SET_NULL, null=True)
    consultant = models.ForeignKey(Doctor,on_delete=models.SET_NULL, null=True)

    photos1  = models.ImageField(upload_to='upload/patient/', blank=True, null=True)
    photos2  = models.ImageField(upload_to='upload/patient/', blank=True, null=True)
    photos3  = models.ImageField(upload_to='upload/patient/', blank=True, null=True)
    photos4  = models.ImageField(upload_to='upload/patient/', blank=True, null=True)

    registration_date = models.DateTimeField(auto_now_add=True)
    last_visit_date = models.DateTimeField(blank=True, null=True)
    Revisit = models.IntegerField(help_text = 'No. of days after want to follow up with Patient.',default=7)


    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.id})"

    class Meta:
        ordering = ['last_name', 'first_name']
