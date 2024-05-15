from django import forms

from ..models.models import CustomUser


class RegistrationForm(forms.ModelForm):

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

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

from ..models.models import DonationTarget


class DonationTargetForm(forms.ModelForm):
    class Meta:
        model = DonationTarget
        fields = ['title', 'description', 'report_expected_due_date', 'donation_requisites', 'donation_target_status', 'donation_target_report']