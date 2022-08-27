
from django.shortcuts import render, redirect
from django.views import View
from main_app.forms import User, UserForm, UserLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
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

def Patient_Request(request):
    return render(request, 'about.html')

def Patient_Details(request):
    # patient = Patient.Patient_id.objects.all()
    return render(request, 'details.html')

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
            return render(request, "home.html")
        else:
            return render(request, "registration/signup.html", {"form": form})

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
            if user is not None:
                login(request, user)
                return render(request, "welcome.html")
            else:
                return render(request, "registration/login.html", {"form": form})
        else:
            return render(request, "registration/login.html", {"form": form})
    
    
class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, "landingpage.html")