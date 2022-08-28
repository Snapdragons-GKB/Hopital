from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model

from main_app.models import Patient, Provider
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
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    usertype = forms.ChoiceField(choices=USERTYPE_CHOICE, required=True)

    class Meta:
        model = User
        USERTYPE_CHOICE = [
            ('Patient', 'Patient'),
            ('Scheduler', 'Scheduler'),
            ('Provider', 'Provider'),
        ]
        fields = ('username', 'password', 'usertype')
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
        error_messages = {
            'username': {
                'unique': "afdf",
            },
            'password': {
                'unique': "asdf",
            },


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
    provider_personal_blurb = forms.CharField(max_length=200)
    provider_specialization = forms.ChoiceField(choices=SPECIALTY_CHOICE, required=True)
    provider_insurances_taken = forms.ChoiceField(choices=INSURANCE_CHOICE, required=True)

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

        model = Provider
        exclude = ('user',)
        fields = ('provider_personal_blurb', 'provider_specialization', 'provider_insurances_taken')
        widgets = {
            'provider_personal_blurb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Personal Blurb'}),
            'provider_specialization': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Specialization'}, choices=SPECIALTY_CHOICE),
            'provider_insurances_taken': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Insurance Taken'}, choices=INSURANCE_CHOICE),
        }
        labels = {
            'provider_personal_blurb': 'Personal Blurb',
            'provider_specialization': 'Specialization',
            'provider_insurances_taken': 'Insurance Taken'
        }
        help_texts = {
            'provider_personal_blurb': None,
            'provider_specialization': None,
            'provider_insurances_taken': None
        }


#Here be dragons
# ---------------------------------------------------------------------------------------------------------------------------------------------------------

class PatientRequest(ModelForm): 
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

    ailment_category = forms.ChoiceField(choices=SPECIALTY_CHOICE, required=True)
    ailment_description = forms.CharField(max_length=200)
