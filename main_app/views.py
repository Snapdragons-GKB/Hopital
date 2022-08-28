
from django.shortcuts import render, redirect
from django.views import View
from main_app.forms import AdditionalPatient, AdditionalProvider, UserForm, UserLogin, PatientRequestForAppointment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from main_app.models import Scheduler, Patient, Provider
# Create your views here.


def Nothing(request):
    return redirect('landing/')

def Landingpage(request): 
    return render(request, 'landingpage.html')

@login_required(redirect_field_name=None)
def Home(request):
    #return render(request, '../main_app/templates/home.html')
    return render(request, 'home.html')

def Welcome(request):
    return render(request, 'welcome.html')

def About(request):
    return render(request, 'about.html')



def Patient_Details(request):
    #got our patient data by calling model
    patientdata = Patient.objects.all()
    #got our current user's id
    ouruserrightnowID = request.user.id
    #iterated through all patients in our data to find a patient with our current user's id
    for patient in patientdata:
        if patient.patientProfile_id == ouruserrightnowID:
            #returned a dictionary with our 
            return render(request, 'details.html', {
                "age":patient.patient_age, 
                "insurance": patient.patient_insurance_type,
                "conditions": patient.patient_preexisting_conditions,
                "medications": patient.patient_current_medications
                })

    return render(request, 'details.html', frozenset('a'))
    
    # return render(request, 'details.html', recastdata)









#classic signup form. On post, signs user in and then checks their usertype, routing to appropriate additionals or home page
class Signup(View): 
    def get(self, request):
        form = UserForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)

            if user.usertype == 'Patient':
                # return render(request, "additional_reg/patient-reg.html", {"form": form})
                return redirect('patient-registration/')
            elif user.usertype == 'Scheduler':
                sched = Scheduler()
                sched.schedulerProfile=request.user
                sched.save() #this may work, check later
                return render(request, "home.html")
            elif user.usertype == 'Provider':
                return redirect('provider-registration/')
        else:
            return render(request, "registration/signup.html", {"form": form})

#The next two methods tender additional details for patient and provider registration.
class Patient_Additional_Reg(View):
    def get(self, request):
        form = AdditionalPatient()
        context = {"form": form}
        return render(request, "additional-reg/patient-reg.html", context)

    def post(self, request):
        form = AdditionalPatient(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.patientProfile = request.user
            patient.save()
            return render(request, "home.html")

        else:
            return render(request, "additional-reg/patient-reg.html", {"form": form})





class Provider_Additional_Reg(View): 
    def get(self, request):
        form = AdditionalProvider()
        context = {"form": form}
        return render(request, "additional-reg/provider-reg.html", context)

    def post(self, request):
        form = AdditionalProvider(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.providerProfile =request.user
            provider.save()
            return render(request, "home.html")

        else:
            return render(request, "additional-reg/provider-reg.html", {"form": form})


#classic login form. On post, checks usertype, routing to separate home page, though that is not built out yet
class Login(View):
    def get(self, request):
        form = UserLogin()
        context = {"form": form}
        return render(request, "registration/login.html", context)

    def post(self, request):
        form = UserLogin(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, "welcome.html")
            # if user is not None:

            #     if user.usertype == 'Patient':
            #         return render(request, "home.html")
            #         #redirect to patient home
            #     elif user.usertype == 'Scheduler':
            #         return render(request, "home.html")
            #         #redirect to scheduler home
            #     elif user.usertype == 'Provider':
            #         return render(request, "home.html")
            #         #redirect to provider home
            #     return render(request, "welcome.html")
            # else:
            #     return render(request, "registration/login.html", {"form": form})
        else:
            return render(request, "registration/login.html", {"form": form})

    
    
    
class Logout(View):
    def get(self, request):
        user=request.user
        if user is not None:
            logout(request)
            return render(request, "landingpage.html")
        return redirect('')

#Here be dragons
###############################################################################################################################

class Patient_Request_Appointment(View):
    def get(self, request):
        form = PatientRequestForAppointment()
        context = {"form": form}
        return render(request, "patient/patient-request.html", context)
        
    def post(self, request):
        form = PatientRequestForAppointment(request.POST)
        if form.is_valid():
            patientrequest = form.save(commit=False)
            patientrequest.patientProfile = request.user
            patientrequest.save()
            return render(request, "welcome.html")
        else:
            return render(request, "patient/patient-request.html", {"form": form})