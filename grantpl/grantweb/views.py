from django.http import JsonResponse
from django.shortcuts import redirect
# from grantpl.grantweb.forms.forms import RegistrationForm, ForgotPasswordForm

from django.shortcuts import render
from django.views.generic import TemplateView

# from grantweb.forms import SignupForm


# class Register(TemplateView):
#
#     template_name = 'registration.html'
#
#     def register(request):
#         if request.method == 'POST':
#             form = RegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.set_password(form.cleaned_data['password'])
#                 user.save()
#                 # Додайте необхідні дії після успішної реєстрації
#         else:
#             form = RegistrationForm()
#         return render(request, 'registration.html', {'form': form})
from .forms.RegistrationForm import RegistrationForm, ForgotPasswordForm
from .models.CustomUser import CustomUser
from .models.User import UserProfile, Messenger
from .services.UserService import check_existing_user


class SignUp(TemplateView):
    template_name = 'registration.html'

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if check_existing_user(email):  # Проверка существующего пользователя
                return render(request, self.template_name,
                              {'form': form, 'error_message': 'Пользователь с таким email уже существует.'})

            account_type = form.cleaned_data['account_type']
            password = form.cleaned_data['password']
            if account_type == 'individual':
                user = CustomUser.objects.create_user(email=email, account_type=account_type, password=password)
            else:
                company_name = form.cleaned_data['company_name']
                company_website = form.cleaned_data['company_website']
                user = CustomUser.objects.create_user(email=email, account_type=account_type, password=password)

                user_profile = UserProfile.objects.create(description="Description")
                messenger = Messenger.objects.create(name="Messenger", actual_id="ID")
                user.user_profile = user_profile
                user_profile.messenger = messenger
                user_profile.save()
                messenger.save()
            return redirect('success_url')
        else:
            forgot_password_form = ForgotPasswordForm(request.POST)
            if forgot_password_form.is_valid():
                email = forgot_password_form.cleaned_data['email']

                return redirect('forgot_password_success_url')
            return render(request, self.template_name, {'form': form, 'forgot_password_form': forgot_password_form})

    def check_existing_user_api(request):

         if request.method == 'POST':

            email = request.POST.get('email')
         if email:
            exists = check_existing_user(email)
            return JsonResponse({'exists': exists})
         return JsonResponse({'error': 'Invalid request'})
class Home(TemplateView):

    template_name = 'mainpage/Главная.html'