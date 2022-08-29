
from django.shortcuts import render, redirect
from django.views import View
from main_app.forms import AdditionalPatient, AdditionalProvider, UserForm, PatientRequestForAppointment, UserLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, get_user_model, login

from main_app.models import Scheduler, Patient, Provider
User=get_user_model()

# Create your views here.


#General views
#If template, found in general-templates folder

def Nothing(request):
    return redirect('landing/')

def Landingpage(request): 
    return render(request, 'general-templates/general-landingpage.html')

def About(request):
    return render(request, 'general-templates/general-about.html')

class Signup(View): 
    def get(self, request):
        form = UserForm()
        context = {"form": form}
        return render(request, "general-templates/general-signup.html", context)

    def post(self, request):
        form = UserForm(data=request.POST)
        context = {"form": form}
        if form.is_valid():
            user = form.save()
            #user.set_password(user.password) the true height of my insanity
            user.save()
            login(request, user)

            if user.usertype == 'Patient':
                 return render(request, "patient-templates/additional-patient-registration.html")
            elif user.usertype == 'Scheduler':
                sched = Scheduler()
                sched.schedulerProfile=request.user
                sched.save()
                return render(request, "scheduler-templates/scheduler-home.html")
            elif user.usertype == 'Provider':
                return render(request, 'provider-templates/additional-provider-registration.html')
        else:
            return render(request, "general-templates/general-signup.html", context)

class Login(View):
    def get(self, request):
        form = UserLogin()
        return render(request, 'general-templates/general-login.html', {'form': form})

    def post(self, request):
        form = UserLogin(data=request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.usertype == 'Patient':
                return render(request, 'patient-templates/patient-home.html')
            elif user.usertype == 'Scheduler':
                return render(request, 'scheduler-templates/scheduler-home.html')
            elif user.usertype == 'Provider':
                return render(request, 'provider-templates/provider-home.html')
        else:
            return render(request, 'general-templates/general-login.html', {'form': form})

class Logout(View):
    def get(self, request):
        user=request.user
        if user is not None:
            logout(request)
            return render(request, "general-templates/general-landingpage.html")




#Patient views
#If template, found in patient-templates folder

def Patient_Home(request):
    return render(request, 'patient-templates/patient-home.html')

def Patient_Welcome(request):
    return render(request, 'patient-templates/patient-welcome.html')

def Patient_Details(request):
    patientdata = Patient.objects.all()
    ouruserrightnowID = request.user.id
    for patient in patientdata:
        print(patient)
        if patient.patientProfile_id == ouruserrightnowID:
            return render(request, 'patient-templates/patient-details.html', {
                "age":patient.patient_age, 
                "insurance": patient.patient_insurance_type,
                "conditions": patient.patient_preexisting_conditions,
                "medications": patient.patient_current_medications
                })

    return render(request, 'patient-templates/patient-details.html')

class Patient_Additional_Reg(View):
    def get(self, request):
        form = AdditionalPatient()
        context = {"form": form}
        return render(request, "patient-templates/additional-patient-registration.html", context)

    def post(self, request):
        form = AdditionalPatient(request.POST)
        context = {"form": form}
        if form.is_valid():
            patient = form.save(commit=False)
            patient.patientProfile = request.user
            patient.save()
            return render(request, "patient-templates/patient-home.html")

        else:
            return render(request, "patient-templates/additional-patient-registration.html", context)


class Patient_Request_Appointment(View):
    def get(self, request):
        form = PatientRequestForAppointment()
        context = {"form": form}
        return render(request, "patient-templates/patient-request.html", context)
        
    def post(self, request):
        form = PatientRequestForAppointment(request.POST)
        context = {"form": form}
        if form.is_valid():
            patientrequest = form.save(commit=False)
            patientrequest.patientProfile = request.user
            patientrequest.save()
            return render(request, "patient-templates/patient-home.html")
        else:
            return render(request, "patient-templates/patient-request.html", context)




#Provider views
#If template, found in provider-templates folder

def Provider_Home(request): 
    return render(request, 'provider-templates/provider-home.html')

def Provider_Welcome(request):
    return render(request, 'provider-templates/provider-welcome.html')

def Provider_Details(request):
    providerdata = Provider.objects.all()
    ouruserrightnowID = request.user.id
    for provider in providerdata:
        if provider.providerProfile_id == ouruserrightnowID:
            return render(request, 'provider-templates/provider-details.html', {
                "blurb": provider.provider_blurb,
                "specialization": provider.provider_specialization,
                "insurances": provider.provider_insurances_taken,
                })

    return render(request, 'provider-templates/provider-details.html')

class Provider_Additional_Reg(View): 
    def get(self, request):
        form = AdditionalProvider()
        context = {"form": form}
        return render(request, "provider-templates/additional-provider-registration.html", context)

    def post(self, request):
        form = AdditionalProvider(request.POST)
        context = {"form": form}
        if form.is_valid():
            provider = form.save(commit=False)
            provider.providerProfile =request.user
            provider.save()
            return render(request, "provider-templates/provider-home.html")

        else:
            return render(request, "provider-templates/additional-provider-registration.html", context)




#Scheduler views
#If template, found in scheduler-templates folder

def Scheduler_Home(request):
    return render(request, 'scheduler-templates/scheduler-home.html')

def Scheduler_Welcome(request):
    return render(request, 'scheduler-templates/scheduler-welcome.html')