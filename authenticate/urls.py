from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import RegistrationView,LoginView,UsernameValidationView,EmailValidationView,LogoutView

urlpatterns=[
    path('register/',csrf_exempt(RegistrationView.as_view()),name='register'),
    path('validate-username/',csrf_exempt(UsernameValidationView.as_view()),name='validate-username'),
    path('validate-email/',csrf_exempt(EmailValidationView.as_view()),name='validate-username'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('client-registration/',views.client_registration,name='client-user-registration'),
    path('client-login/',views.ClientLogin,name='client-user-login')
]