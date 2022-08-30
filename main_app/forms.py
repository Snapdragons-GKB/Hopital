from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model

from main_app.models import Encounter, Patient, Provider, PatientRequestForAppointment
User = get_user_model()


class UserForm(UserCreationForm):
    USERTYPE_CHOICE = [
        ('Patient', 'Patient'),
        ('Scheduler', 'Scheduler'),
        ('Provider', 'Provider'),
    ]
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    usertype = forms.ChoiceField(choices=USERTYPE_CHOICE, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        
        USERTYPE_CHOICE = [
            ('Patient', 'Patient'),
            ('Scheduler', 'Scheduler'),
            ('Provider', 'Provider')
        ]
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'usertype', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
            'usertype': forms.Select(attrs={'class': 'form-control', 'placeholder': 'usertype'}, choices=USERTYPE_CHOICE),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'usertype': 'Usertype'
        }
        help_texts = {
            'username': None,
            'email': None,
            'first_name': None,
            'last_name': None,
            'password1': None,
            'password2': None,
            'usertype': None
        }
        error_messages = {
            'username': {
                'unique': "A user with that username already exists.",
            },
            'email': {
                'unique': "A user with that email already exists.",
            },

        }






class UserLogin(AuthenticationForm):
    USERTYPE_CHOICE = [
        ('Patient', 'Patient'),
        ('Scheduler', 'Scheduler'),
        ('Provider', 'Provider'),
    ]
    username = forms.CharField(max_length=30, required=False)
    password = forms.PasswordInput()
    usertype = forms.ChoiceField(choices=USERTYPE_CHOICE, required=False)

    class Meta:
        
        USERTYPE_CHOICE = [
            ('Patient', 'Patient'),
            ('Scheduler', 'Scheduler'),
            ('Provider', 'Provider'),
        ]
        fields = ('usertype', 'username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'usertype': forms.Select(attrs={'class': 'form-control', 'placeholder': 'usertype'}, choices=USERTYPE_CHOICE),
        }
        labels = {
            'username': 'Username',
            'password': 'Password',
            'usertype': 'User Type'
        }
        help_texts = {
            'username': None,
            'password': None,
            'usertype': None
        }
        


        











class AdditionalPatient(ModelForm):
    INSURANCE_CHOICE = [
        ('Without Insurance', 'Without Insurance'),
        ('Medicaid', 'Medicaid'),
        ('Medicare', 'Medicare'),
        ('Private', 'Private'),
    ]
    patient_age = forms.IntegerField()
    # patient_insurance_type = forms.CharField(max_length=20, choices=INSURANCE_CHOICE.choices, default=INSURANCE_CHOICE.choices[0][0])
    patient_insurance_type = forms.ChoiceField(choices=INSURANCE_CHOICE, required=True)
    patient_preexisting_conditions = forms.CharField(max_length=200)
    patient_current_medications = forms.CharField(max_length=200)

    class Meta:
        INSURANCE_CHOICE = [
            ('Without Insurance', 'Without Insurance'),
            ('Medicaid', 'Medicaid'),
            ('Medicare', 'Medicare'),
            ('Private', 'Private'),
        ]
        model = Patient
        exclude = ['user']
        fields = ('patient_age', 'patient_insurance_type', 'patient_preexisting_conditions', 'patient_current_medications')
        widgets = {
            'patient_age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'patient_insurance_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Insurance Type'}, choices=INSURANCE_CHOICE),
            'patient_preexisting_conditions': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preexisting Conditions'}),
            'patient_current_medications': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Medications'}),
        }
        labels = {
            'patient_age': 'Age',
            'patient_insurance_type': 'Insurance Type',
            'patient_preexisting_conditions': 'Preexisting Conditions',
            'patient_current_medications': 'Current Medications'
        }
        help_texts = {
            'patient_age': None,
            'patient_insurance_type': None,
            'patient_preexisting_conditions': None,
            'patient_current_medications': None
        }












class AdditionalProvider(ModelForm):
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
        ('Available', 'Available')

    ]
    provider_personal_blurb = forms.CharField(max_length=200)
    provider_specialization = forms.ChoiceField(choices=SPECIALTY_CHOICE,  initial=AVAILABILITY_CHOICES[0])
    provider_insurances_taken = forms.ChoiceField(choices=INSURANCE_CHOICE,  initial=AVAILABILITY_CHOICES[0])
    monday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    tuesday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    wednesday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    thursday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    friday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    saturday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])
    sunday = forms.ChoiceField(choices=AVAILABILITY_CHOICES,  initial=AVAILABILITY_CHOICES[1])

    class Meta:
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
        ('Available', 'Available')
        #note we only allow them to choose non filled options
        ]

        model = Provider
        exclude = ['providerProfile']
        fields = ('provider_personal_blurb', 'provider_specialization', 'provider_insurances_taken', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        widgets = {
            'provider_personal_blurb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Personal Blurb'}),
            'provider_specialization': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Specialization'}, choices=SPECIALTY_CHOICE),
            'provider_insurances_taken': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Insurance Taken'}, choices=INSURANCE_CHOICE),
            'monday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Monday'}, choices=AVAILABILITY_CHOICES),
            'tuesday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tuesday'}, choices=AVAILABILITY_CHOICES),
            'wednesday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Wednesday'}, choices=AVAILABILITY_CHOICES),
            'thursday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Thursday'}, choices=AVAILABILITY_CHOICES),
            'friday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Friday'}, choices=AVAILABILITY_CHOICES),
            'saturday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Saturday'}, choices=AVAILABILITY_CHOICES),
            'sunday': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sunday'}, choices=AVAILABILITY_CHOICES),
        }
        labels = {
            'provider_personal_blurb': 'Personal Blurb',
            'provider_specialization': 'Specialization',
            'provider_insurances_taken': 'Insurance Taken',
            'monday': 'Monday',
            'tuesday': 'Tuesday',
            'wednesday': 'Wednesday',
            'thursday': 'Thursday',
            'friday': 'Friday',
            'saturday': 'Saturday',
            'sunday': 'Sunday'


        }
        help_texts = {
            'provider_personal_blurb': None,
            'provider_specialization': None,
            'provider_insurances_taken': None,
            'monday': None,
            'tuesday': None,
            'wednesday': None,
            'thursday': None,
            'friday': None,
            'saturday': None,
            'sunday': None
        }


#Here be dragons
#Don't depend on anything below here
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

class PatientRequestForAppointment(ModelForm):
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
    #native adds not included 

    #patient entered
    patient_ailment_category = forms.ChoiceField(choices=ailment_category, required=True)
    patient_ailment_description = forms.CharField(max_length=200)
    patient_preferred_day = forms.ChoiceField(choices=DAY_OF_ENCOUNTER_CHOICES, required=True)


    class Meta:
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
        model = PatientRequestForAppointment
        exclude = ['patientUser', 'schedulerUser', 'accepted',]
        fields = ('patient_ailment_category', 'patient_ailment_description', 'patient_preferred_day')
        widgets = {
            'patient_ailment_category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ailment Category'}, choices=ailment_category),
            'patient_ailment_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ailment Description'}),
            'patient_preferred_day': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Preferred Day'}, choices=DAY_OF_ENCOUNTER_CHOICES),
        }
        labels = {
            'patient_ailment_category': 'Ailment Category',
            'patient_ailment_description': 'Ailment Description',
            'patient_preferred_date': 'Preferred Date Range Start',
        }
        help_texts = {
            'patient_ailment_category': None,
            'patient_ailment_description': None,
            'patient_preferred_date': None,
        }

        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
#New stuff after remote chopped
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# class EncounterCreation(ModelForm):
    
#     DAY_OF_ENCOUNTER_CHOICES = [
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#         ('Saturday', 'Saturday'),
#         ('Sunday', 'Sunday'),
#     ]
#     DOCTOR_OF_ENCOUNTER_CHOICES = Provider.objects.get(data[data.day]=User.objects.get(username='doctor1')),
#     #native adds not included 

#     #patient entered
#     encounter_date = forms.CharField(choices=DAY_OF_ENCOUNTER_CHOICES, required=True)


#     class Meta:
        
#         DAY_OF_ENCOUNTER_CHOICES = [
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#         ('Saturday', 'Saturday'),
#         ('Sunday', 'Sunday'),
#     ]
#         model = Encounter
#         exclude = ['patientUser', 'providerUser', 'doctor_comment', 'doctor_comment', 'patient_comment']

