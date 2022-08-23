from django.urls import path
from . import views

#create routes for patient portal, maps to views.py
urlpatterns=[
    path('', views.Home.as_view(), name='home'), 
    path('patient_request/',views.Patient_Request.as_view(), name='patient_request'), 
    path('patient/<int:patientID>/detail/', views.Patient_details.as_view(), name='patient_detail'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
   

#create routes for Scheduler/Admin portal
    path('admin/', views.Home_Admin.as_views(), name='admin'),
    path('admin/patient_request/', views.Admin_Patient_Request.as_view(), name='admin_patient_request'),
    path('admin/patient_list/', views.Admin_Patient_list.as_view(), name='admin_patient_list'),

#create routes for Provider portal
    path('provider/', views.Home_Provider.as_view(), name='provider'),
    path('provider/schedule', views.Schedule.as_view(), name='schedule'),
    path('provider/client_list', views.Provider_client_list.as_views(), name='client_list')


    
]


