from urllib import request

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from ..forms.Grant import GrantFilterForm
from ..forms.RegistrationForm import LoginForm, RegistrationForm
from ..models.models import User, UserType, Role, UserProfile, Messenger, Grant, DonationTarget, DonationTargetReport


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        account_type = request.POST.get('account_type')

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists'})

        try:
            default_role = Role.objects.get(role='individual')
        except Role.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Default role does not exist'})

        try:
            default_user_type = UserType.objects.first()
            if not default_user_type:
                default_user_type = UserType.objects.create(type='default_type')
        except UserType.DoesNotExist:
            default_user_type = UserType.objects.create(type='default_type')

        try:
            default_messenger = Messenger.objects.first()
            if not default_messenger:
                default_messenger = Messenger.objects.create(name='default', actual_id='default_id')
        except Messenger.DoesNotExist:
            default_messenger = Messenger.objects.create(name='default', actual_id='default_id')

        user_profile = UserProfile.objects.create(
            description='',
            messenger=default_messenger
        )

        user = User.objects.create(
            email=email,
            password=password,
            salt='random_salt',
            role=default_role,
            user_profile=user_profile,
            user_type=default_user_type
        )
        if account_type == 'individual':
            return HttpResponseRedirect('/individual/')
        elif account_type == 'organization':
            return HttpResponseRedirect('/organization/')
        else: JsonResponse({'success': True, 'message': 'User registered successfully'})
    else:
        return render(request, 'register.html')
    #     password = request.POST.get('password')
    #
    #
    #     if User.objects.filter(email=email).exists():
    #         return JsonResponse({'success': False, 'message': 'Email already exists'})
    #
    #
    #
    #
    #
    #
    #
    #     # Створення нового користувача
    #     user = User(
    #         email=email,
    #         password=password,
    #
    #
    #     )
    #     user.save()
    #
    #     return JsonResponse({'success': True})
    # else:
    #     return render(request, 'register.html')
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'User with this email does not exist'})

            if user.check_password(password):
                request.session['user_id'] = user.id

                if user.account_type == 'individual':
                    return redirect('personal_dashboard')
                elif user.account_type == 'organization':
                    return redirect('organizational_dashboard')
                else:
                    return JsonResponse({'success': False, 'message': 'Unknown account type'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data'})
    else:
        form = LoginForm()
        return render(request, 'registration.html', {'form': form})
class SignUp(TemplateView):
    template_name = 'registration.html'




class Home(TemplateView):

    template_name = 'mainpage/Главная.html'


def grant_list(request):
    form = GrantFilterForm(request.GET or None)
    grants = Grant.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')


        if search:
            grants = grants.filter(name__icontains=search)



    return render(request, 'grant_list.html', {'grants': grants, 'form': form})

def submit_report(request):
    if request.method == 'POST':
        report_text = request.POST.get('report')
        donation_target_id = request.POST.get('donation_target_id')
        file = request.FILES.get('files')

        donation_target = DonationTarget.objects.get(id=donation_target_id)
        DonationTargetReport.objects.create(
            report=report_text,
            files=file,
            donation_target=donation_target
        )

        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'error'}, status=400)