from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


#create routes for patient portal, maps to views.py
urlpatterns=[
    #initial definitions for portal
    path('', views.Nothing, name='nothing'), #A redirect to the landing page
    path('landing/', views.Landingpage, name='home'), #The landing page for everyone
    
    #holy trinity of actions, defined in views.py
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),


    #routes for additional patient/provider registration
    path('signup/patient-registration/', views.Patient_Additional_Reg.as_view(), name="patient-registration"),
    path('signup/provider-registration/', views.Provider_Additional_Reg.as_view(), name="provider-registration"),

    #somewhat diffusely defined behaviors for before/after login, treat with some skepticism
    path('home/', views.Home, name='home'), 
    path('welcome/', views.Welcome, name="welcome"),
    path('about/', views.About, name="about"),
    

    #route for testing patient request
    path('patient/request/', views.Patient_Request_Appointment.as_view(), name='patient_request'),
    path('patient/detail/', views.Patient_Details, name='patient_detail'), 



#create routes for Scheduler/Admin portal
    # path('admin/', views.Home_Admin, name='admin'),
    # path('admin/patient_request/', views.Admin_Patient_Request.as_view(), name='admin_patient_request'),
    # path('admin/patient_list/', views.Admin_Patient_list.as_view(), name='admin_patient_list'),

#create routes for Provider portal
    path('provider/', views.Provider_Home, name='provider'),
    # path('provider/schedule', views.Provider_Schedule, name='schedule'),
    # path('provider/client_list', views.Provider_Clientlist, name='client_list')


    
]


