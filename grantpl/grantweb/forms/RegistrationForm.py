from django import forms

from grantweb.models.CustomUser import CustomUser


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'account_type', 'password', 'company_name', 'company_website']
        widgets = {
            'password': forms.PasswordInput(),
            'account_type': forms.RadioSelect(choices=CustomUser.ACCOUNT_TYPE_CHOICES),
        }

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email')
# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("name", "email")
#         field_classes = {'name': UsernameField}