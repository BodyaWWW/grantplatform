from django import forms

from ..models.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),

        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email')
# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("name", "email")
#         field_classes = {'name': UsernameField}