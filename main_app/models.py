
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
    providerProfile = models.OneToOneField(User, on_delete=models.CASCADE)
    provider_personal_blurb = models.CharField(max_length=200)
    provider_specialization = models.CharField(max_length=20, choices=SPECIALTY_CHOICE, default=SPECIALTY_CHOICE[0][0])
    provider_insurances_taken = models.CharField(max_length=20, choices=INSURANCE_CHOICE, default=INSURANCE_CHOICE[0][0])
    day1 = models.BooleanField(default=False)
    day2 = models.BooleanField(default=False)
    day3 = models.BooleanField(default=False)
    day4 = models.BooleanField(default=False)
    day5 = models.BooleanField(default=False)
    day6 = models.BooleanField(default=False)
    day7 = models.BooleanField(default=False)

    


# class PatientRequest(models.Model):
#     class request_status(models.TextChoices):
#         SUBMITTED = 0, 'Awating Response'
#         ACCEPTED = 1, 'Accepted'
#         REJECTED = 2, 'Rejected'
#         COMPLETED = 3, 'Completed'
    
#     class ailment_category(models.TextChoices):
#         NONE = 0, 'None'
#         GENERAL_MEDICINE = 1, 'General Medicine'
#         ORTHOPEDICS = 2, 'Orthopedics'
#         CARDIOLOGY = 3, 'Cardiology'
#         NEUROLOGY = 4, 'Neurology'
#         PEDIATRICS = 5, 'Pediatrics'
#         EMERGENCY = 6, 'Emergency'
#         PSYCHIATRY = 7, 'Psychiatry'
#         RADIOLOGY = 8, 'Radiology'
#         INTERNAL_MEDICINE = 9, 'Internal Medicine'
#         OTHER = 10, 'Other'


#     request_status = models.CharField(max_length=20, choices=request_status.choices, default=request_status.SUBMITTED)
    
#     request_patient_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patientofrequest')
#     request_scheduler_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedulerofrequest', default=None)
#     request_doctor_profile= models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctorofrequest', default=None)
    
#     request_ailment_category = models.CharField(max_length=20, choices=ailment_category.choices, default=ailment_category.NONE)
#     request_ailment_description = models.CharField(max_length=80)
    
#     request_preferred_date_range_start = models.DateField()
#     request_preferred_date_range_end = models.DateField()

#     request_procedure_date = models.DateField()
#     request_scheduling_comment = models.TextField(default=None)

#     request_doctor_comment_on_operation = models.TextField(default=None)




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
    
    #natively added
    patientProfile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patientofrequest')
    patientInsuranceType = models.CharField(max_length=20, choices=Patient.INSURANCE_CHOICE, default=Patient.INSURANCE_CHOICE[0][0])


    #patient entered
    patient_ailment_category = models.CharField(max_length=20, choices=ailment_category, default=ailment_category[0][0])
    patient_ailment_description = models.CharField(max_length=80)
    patient_preferred_date = models.DateField()


    