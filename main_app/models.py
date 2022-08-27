
from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """
    Adding additional fields to the default User model.
    """
    USERTYPE_CHOICE = [
            ('Patient', 'Patient'),
            ('Scheduler', 'Scheduler'),
            ('Provider', 'Provider'),
        ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254 )
    usertype = models.CharField(choices=USERTYPE_CHOICE, max_length=15, default='Patient')




    

class Patient(models.Model):
    class insurance(models.TextChoices):
        NONE = 0, 'Without Insurance'
        MEDICAID = 1, 'Medicaid'
        MEDICARE = 2, 'Medicare'
        PRIVATE = 3, 'Private'

    
    #patientProfile = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    patient_age = models.IntegerField()
    patient_insurance_type = models.CharField(max_length=20, choices=insurance.choices, default=insurance.NONE)
    patient_preexisting_conditions = models.TextField(max_length=80)
    patient_current_medications = models.TextField(max_length=80)

class Scheduler(models.Model):
    schedulerProfile = models.TextField(max_length=80)

class Provider(models.Model):
    class insurance(models.TextChoices):
        NONE = 0, 'Without Insurance'
        MEDICAID = 1, 'Medicaid'
        MEDICARE = 2, 'Medicare'
        PRIVATE = 3, 'Private'

    class specialty(models.TextChoices):
        NONE = 0, 'None'
        CARDIOLOGY = 1, 'Cardiology'
        NEUROLOGY = 2, 'Neurology'
        PEDIATRICS = 3, 'Pediatrics'
        SURGERY = 4, 'Surgery'
        DENTAL = 5, 'Dental'
        GENERAL_MEDICINE = 6, 'General Medicine'
        PSYCHIATRY = 7, 'Psychiatry'
        RADIOLOGY = 8, 'Radiology'
        SURGICAL = 9, 'Surgical'
        OTHER = 10, 'Other'

    #providerProfile = models.OneToOneField(User, on_delete=models.CASCADE)
    
    provider_personal_blurb = models.CharField(max_length=200)
    provider_specialization = models.CharField(max_length=20, choices=specialty.choices, default=specialty.NONE)
    provider_insurances_taken = models.CharField(max_length=20, choices=insurance.choices, default=insurance.NONE)
    day1 = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)

    


class PatientRequest(models.Model):
    class request_status(models.TextChoices):
        SUBMITTED = 0, 'Awating Response'
        ACCEPTED = 1, 'Accepted'
        REJECTED = 2, 'Rejected'
        COMPLETED = 3, 'Completed'
    
    class ailment_category(models.TextChoices):
        NONE = 0, 'None'
        CARDIOLOGY = 1, 'Cardiology'
        NEUROLOGY = 2, 'Neurology'
        PEDIATRICS = 3, 'Pediatrics'
        SURGERY = 4, 'Surgery'
        DENTAL = 5, 'Dental'
        GENERAL_MEDICINE = 6, 'General Medicine'
        PSYCHIATRY = 7, 'Psychiatry'
        RADIOLOGY = 8, 'Radiology'
        SURGICAL = 9, 'Surgical'
        OTHER = 10, 'Other'


    request_status = models.CharField(max_length=20, choices=request_status.choices, default=request_status.SUBMITTED)
    
    request_patient_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patientofrequest')
    request_scheduler_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedulerofrequest', default=None)
    request_doctor_profile= models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctorofrequest', default=None)
    
    request_ailment_category = models.CharField(max_length=20, choices=ailment_category.choices, default=ailment_category.NONE)
    request_ailment_description = models.CharField(max_length=80)
    
    request_preferred_date_range_start = models.DateField()
    request_preferred_date_range_end = models.DateField()

    request_procedure_date = models.DateField()
    request_scheduling_comment = models.TextField(default=None)

    request_doctor_comment_on_operation = models.TextField(default=None)

