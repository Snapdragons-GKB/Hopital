from django.urls import path
from . import views

#create routes for patient portal, maps to views.py
urlpatterns=[
    path('', views.Nothing, name='nothing'),
    path('landing/', views.Landingpage, name='home'),
    path('home/', views.Home, name='home'), 
    path('patient/request/',views.Patient_Request, name='patient_request'), 
    path('patient/detail/', views.Patient_Details, name='patient_detail'), # needs to be added to path once db seeded
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('welcome/', views.Welcome, name="welcome"),
    path('about/', views.About, name="about"),
    path('logout/', views.Logout.as_view(), name="logout"),

#create routes for Scheduler/Admin portal
    # path('admin/', views.Home_Admin, name='admin'),
    # path('admin/patient_request/', views.Admin_Patient_Request.as_view(), name='admin_patient_request'),
    # path('admin/patient_list/', views.Admin_Patient_list.as_view(), name='admin_patient_list'),

#create routes for Provider portal
    # path('provider/', views.Home_Provider.as_view(), name='provider'),
    # path('provider/schedule', views.Schedule.as_view(), name='schedule'),
    # path('provider/client_list', views.Provider_client_list.as_views(), name='client_list')


    
]


