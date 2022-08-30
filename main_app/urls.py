from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    #General patterns
    #If template, found in general-templates folder
    path('', views.Nothing, name='nothing'), #A redirect to the landing page
    path('landing/', views.Landingpage, name='landing'), #The landing page
    path('signup/', views.Signup.as_view(), name='signup'), #The signup page
    path('login/', views.Login.as_view(), name='login'), #The login page
    path('logout/', views.Logout.as_view(), name='logout'), #The logout page
    path('about/', views.About, name='about'), #The about page


    #Patient patterns
    #If template, found in patient-templates folder
    path('patient/patient-registration/', views.Patient_Additional_Reg.as_view(), name="patient-registration"),
    path('patient/home/', views.Patient_Home, name="patient-home"),
    path('patient/request/', views.Patient_Request_Appointment.as_view(), name="patient-request"),
    path('patient/detail/', views.Patient_Details, name="patient-detail"),
    path('patient/requesthistory/', views.Patient_Request_History, name="patient-request-history"),
    #Provider patterns
    #If template, found in provider-templates folder
    path('provider/provider-registration/', views.Provider_Additional_Reg.as_view(), name="provider-registration"),
    path('provider/home/', views.Provider_Home, name="provider-home"),
    path('provider/detail/', views.Provider_Details, name="provider-detail"),
    path('provider/schedule/', views.Provider_Schedule, name="provider-schedule"),
    
    
    #Scheduler patterns
    #If template, found in scheduler-templates folder
    path('scheduler/home/', views.Scheduler_Home, name="scheduler-home"),
    path('scheduler/work/', views.Scheduler_Work, name="scheduler-work"),




    
]


