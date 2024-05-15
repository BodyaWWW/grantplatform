from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from ..forms.RegistrationForm import LoginForm, RegistrationForm
from ..models.models import CustomUser, User


def register(request):
    print('register method')
    if request.method=='POST':
        print('register')
        email = request.POST.get('email')
        password = request.POST.get('password')
        account_type = request.POST.get('account_type')
        print(email,password,account_type)

        user_record = User(email,password)
        user_record.save()
        #     if form.is_valid():
    #         print('form is valid')
    #         form.save()
    #         email = form.cleaned_data.get('email')
    #         raw_password = form.cleaned_data.get('password')
    #         account_type = form.cleaned_data.get('account_type')
    #         user_record = User(email=email, password=raw_password)
    #         user_record.save()
    #         if account_type == 'personal':
    #             return redirect('personal_dashboard')
    #         elif account_type == 'organizational':
    #             return redirect('organizational_dashboard')
    # elif 'login' in request.POST:
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(email=email, password=password)
    #         if user is not None:
    #             # login(request, user)
    #             account_type = user.account_type
    #             print(account_type)
    #             if account_type == 'personal':
    #                 return redirect('personal_dashboard')
    #             elif account_type == 'organizational':
    #                 return redirect('organizational_dashboard')
    else:
        form = RegistrationForm()  # or LoginForm() depending on the situation
    return render(request, 'registration.html', {'form': form})

class SignUp(TemplateView):
    template_name = 'registration.html'

    def post(self, request, *args, **kwargs):
        if 'register_form' in request.POST:
            print('register')
            form = RegistrationForm(request.POST)
            if form.is_valid():
                print('form is valid')
                form.save()
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                account_type = form.cleaned_data.get('account_type')
                user_record = User(email=email,password=raw_password)
                user_record.save()
                if account_type == 'personal':
                    return redirect('personal_dashboard')
                elif account_type == 'organizational':
                    return redirect('organizational_dashboard')
        elif 'login' in request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None:
                    # login(request, user)
                    account_type = user.account_type
                    print(account_type)
                    if account_type == 'personal':
                        return redirect('personal_dashboard')
                    elif account_type == 'organizational':
                        return redirect('organizational_dashboard')
        else:
            form = RegistrationForm()  # or LoginForm() depending on the situation
        return render(request, 'registration.html', {'form': form})



class Home(TemplateView):

    template_name = 'mainpage/Главная.html'