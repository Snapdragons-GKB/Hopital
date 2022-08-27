from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        fields = ('username', 'email', 'first_name', 'last_name','usertype', 'password1', 'password2')
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
        fields = ('username','password', 'usertype')
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