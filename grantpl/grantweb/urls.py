
from django.urls import path

from .views import views
from .views.DonationTarget import DonationCreate
from .views.Organization_dashboard_view import Organization_Dashboard
from .views.Personal_dashboard_view import Personal_Dashboard,Profile
from .views.views import Home, SignUp


urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('registerform/', SignUp.as_view(), name='register_form'),
    path('personal/', Personal_Dashboard.as_view(), name='personal_dashboard'),
    path('organizational/', Organization_Dashboard.as_view(), name='organizational_dashboard'),
    path('donationcreate/', DonationCreate.as_view(), name = 'donation_create'),
    path('profile/', Profile.as_view(), name = 'profile'),
]