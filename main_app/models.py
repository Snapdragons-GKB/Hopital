
from calendar import TUESDAY

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
    INSURANCE_CHOICE = [
        ('Without Insurance', 'Without Insurance'),
        ('Medicaid', 'Medicaid'),
        ('Medicare', 'Medicare'),
        ('Private', 'Private'),
    ]
    
    patientProfile = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    patient_age = models.IntegerField()
    patient_insurance_type = models.CharField(max_length=20, choices=INSURANCE_CHOICE, default=INSURANCE_CHOICE[0][0])
    patient_preexisting_conditions = models.TextField(max_length=80)
    patient_current_medications = models.TextField(max_length=80)

class Scheduler(models.Model):
    schedulerProfile = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)


class Provider(models.Model):
    SPECIALTY_CHOICE = [
        ('None', 'None'),
        ('General', 'General'),
        ('Orthopedics', 'Orthopedics'),
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Pediatrics', 'Pediatrics'),
        ('Emergency', 'Emergency'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiology', 'Radiology'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Other', 'Other'),
    ]
    INSURANCE_CHOICE = [
        ('Without Insurance', 'Without Insurance'),
        ('Medicaid', 'Medicaid'),
        ('Medicare', 'Medicare'),
        ('Private', 'Private'),
    ]
    AVAILABILITY_CHOICES = [
        ('Unavailable', 'Unavailable'),
        ('Available', 'Available'),
        ('Filled', 'Filled'),
    ]
    providerProfile = models.OneToOneField(User, on_delete=models.CASCADE)
    provider_personal_blurb = models.CharField(max_length=200)
    provider_specialization = models.CharField(max_length=20, choices=SPECIALTY_CHOICE, default=SPECIALTY_CHOICE[0][0])
    provider_insurances_taken = models.CharField(max_length=20, choices=INSURANCE_CHOICE, default=INSURANCE_CHOICE[0][0])
    monday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    tuesday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    wednesday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    thursday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    friday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    saturday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])
    sunday = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=AVAILABILITY_CHOICES[0][0])

    

#Here be dragons
###############################################################################################################################

class PatientRequestForAppointment(models.Model):
    ailment_category = [
        ('None', 'None'),
        ('General', 'General'),
        ('Orthopedics', 'Orthopedics'),
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Pediatrics', 'Pediatrics'),
        ('Emergency', 'Emergency'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiology', 'Radiology'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Other', 'Other'),
        ]
    DAY_OF_ENCOUNTER_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    #natively added
    patientUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patientofrequest')
    patientInsuranceType = models.CharField(max_length=20, choices=Patient.INSURANCE_CHOICE, default=Patient.INSURANCE_CHOICE[0][0])
    patientFirst = models.CharField(max_length=20)
    patientLast = models.CharField(max_length=20)
    #patient entered
    patient_ailment_category = models.CharField(max_length=20, choices=ailment_category, default=ailment_category[0][0])
    patient_ailment_description = models.CharField(max_length=80) 
    patient_preferred_day = models.CharField(max_length=20, choices=DAY_OF_ENCOUNTER_CHOICES, default=DAY_OF_ENCOUNTER_CHOICES[0][0])

    #scheduler data entered later, separate forms
    schedulerUser = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='schedulerofrequest', blank = True, null=True)
    accepted = models.BooleanField(blank=True, null=True)
    scheduler_comment = models.CharField(max_length=200, blank=True, null=True)

class Encounter(models.Model):
    DAY_OF_ENCOUNTER_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    schedulerUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='schedulerofencounter')
    patientUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='patientofencounter')
    providerUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='providerofencounter')
    description = models.CharField(max_length=200, blank=True, null=True)
    encounter_date = models.CharField(max_length=20, choices=DAY_OF_ENCOUNTER_CHOICES, default=DAY_OF_ENCOUNTER_CHOICES[0][0])
    doctor_comment = models.TextField(default=None, blank=True, null=True)
    patient_comment = models.TextField(default=None, blank=True, null=True)