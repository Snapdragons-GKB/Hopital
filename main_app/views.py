
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

def Approve(request):
    return render(request, 'approve.html')

def Reject(request):
    return render(request, 'reject.html')



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


def Pending_Requests(request):
    pendingrequests = PatientRequestForAppointment.objects.all()
    for allrequests in pendingrequests:
            return render(request, 'details.html', {
                "ailment_category": allrequests.ailment_category, 
                "insurance": allrequests.patientInsuranceType,
                "conditions": allrequests.patient_preferred_date,
                })
    return render(request, 'pendingrequests.html', frozenset('a'))




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
                return render(request, "pendingrequests.html")
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
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = UserLogin(data=request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            print("glorious")
            login(request, user)
            return redirect('home')
        # if user.check_password(request.POST['password']):
        #     login(request, user)
        #     return redirect('home')
        # print(user)
        else:
            print("fail")
            return render(request, 'registration/login.html', {'form': form})


        
    
    
    
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