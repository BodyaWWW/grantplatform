
from django.urls import path,include
from .views import Home,SignUp

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('register/', SignUp.as_view(), name='register'),

]