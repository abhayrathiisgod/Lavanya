from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctor(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = models.IntegerField(default=0)

    # Contact Information
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    id_proof_type = models.CharField(max_length=50, choices=[('Nagrikta', 'Nagrikta'), ('Passport', 'Passport'), ('Driver\'s License', 'Driver\'s License'), ('Voter ID', 'Voter ID')])
    id_proof_number = models.CharField(max_length=50)
    id_proof_document = models.FileField(upload_to='identity_proofs/', blank=True, null=True)

    # Professional Information

    license_number = models.CharField(max_length=50, unique=True)
    license_expiry_date = models.DateField()
    specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    years_of_experience = models.IntegerField()
    current_hospital = models.CharField(max_length=100, blank=True, null=True)
    previous_hospitals = models.TextField(blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)

    # Schedule Information
    available_days = models.CharField(max_length=100, help_text="Comma-separated list of available days (e.g., Monday, Wednesday, Friday)")
    available_from_time = models.TimeField()
    available_to_time = models.TimeField()

    # Registration Information
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Additional Information
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} (Specialization: {self.specialization})"

    class Meta:
        ordering = ['last_name', 'first_name']


class Nurse(Doctor):

    # Certificate Files
    certificate_1 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_2 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_3 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_4 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_5 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_6 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_7 = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_7 = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"Nurse {self.first_name} {self.last_name} (Specialization: {self.specialization})"

    class Meta:
        ordering = ['last_name', 'first_name']


class NormalEmployee(models.Model):
    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])

    # Contact Information
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    # Professional Information
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')

    # Identity Proof Documents
    id_proof_type = models.CharField(max_length=50, choices=[('Nagrikta', 'Nagrikta'), ('Passport', 'Passport'), ('Driver\'s License', 'Driver\'s License'), ('Voter ID', 'Voter ID')])
    id_proof_number = models.CharField(max_length=50)
    id_proof_document = models.FileField(upload_to='identity_proofs/', blank=True, null=True)

    # Registration Information
    registered_by = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Additional Information
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Employee ID: {self.employee_id})"

    class Meta:
        ordering = ['last_name', 'first_name']