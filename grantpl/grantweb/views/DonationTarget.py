# views.py
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

# from ..forms.DonationCreate import FundraiserForm, DonationRequisitesForm, DonationTargetReportForm
from ..forms.DonationFilter import DonationTargetFilterForm
from ..forms.forms import DonationTargetForm  # Проверьте путь к вашей форме
from ..models.models import DonationTarget, DonationRequisites, DonationTargetStatus, \
    DonationTargetReport, User  # Проверьте путь к вашей модели
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils import timezone


def create_fundraiser(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        report_expected_due_date = request.POST.get('report_expected_due_date')
        requisites_monobank_jar = request.POST.get('requisites_monobank_jar')
        requisites_iban = request.POST.get('requisites_iban')
        requisites_paypal = request.POST.get('requisites_paypal')

        # Проверка наличия обязательных полей
        if title and description and report_expected_due_date and requisites_monobank_jar and requisites_iban or requisites_paypal:
            default_status = DonationTargetStatus.objects.get_or_create(status='На рассмотрении')[0]

            # Создание DonationRequisites
            requisites = DonationRequisites.objects.create(
                requisites_monobank_jar=requisites_monobank_jar,
                requisites_iban=requisites_iban,
                requisites_paypal=requisites_paypal,
            )

            # Создание DonationTarget без пользователя
            donation_target = DonationTarget.objects.create(
                title=title,
                description=description,
                created_at=timezone.now(),
                report_expected_due_date=report_expected_due_date,
                donation_requisites=requisites,  # Использование созданных реквизитов
                donation_target_status=default_status,
            )

            # Создание пустого DonationTargetReport
            donation_target_report = DonationTargetReport.objects.create(
                report="Ожидается отчет",  # Исходный текст репорта можно заменить на любой дефолтный текст
                donation_target=donation_target,
            )

            # Обновление donation_target с созданным donation_target_report
            donation_target.donation_target_report = donation_target_report
            donation_target.save()

            # Перезагрузка страницы с обновленным списком сборов
            fundraisers = DonationTarget.objects.all()
            return render(request, 'donation_create.html', {'fundraisers': fundraisers})

        else:
            return JsonResponse({'success': False, 'error': 'All fields are required'}, status=400)

    else:
        fundraisers = DonationTarget.objects.all()
        return render(request, 'donation_create.html', {'fundraisers': fundraisers})

class DonationList(TemplateView):
    def donation_targets_list(request):
        donation_targets = DonationTarget.objects.all()
        filter_form = DonationTargetFilterForm(request.GET)

        if filter_form.is_valid():
            status = filter_form.cleaned_data.get('status')
            if status:
                donation_targets = donation_targets.filter(donation_target_status__status=status)

        return render(request, 'donation_targets_list.html',
                      {'donation_targets': donation_targets, 'filter_form': filter_form})


    def my_donation_targets(request):
        user = request.user
        donation_targets = DonationTarget.objects.filter(user=user)

        return render(request, 'my_donation_targets.html', {'donation_targets': donation_targets})

# class DonationCreate(TemplateView):
#
#     template_name = 'donation_create.html'
#
#     def create_fundraiser(request):
#         if request.method == 'POST':
#             fundraiser_form = FundraiserForm(request.POST)
#             requisites_form = DonationRequisitesForm(request.POST)
#             report_form = DonationTargetReportForm(request.POST, request.FILES)
#             if fundraiser_form.is_valid() and requisites_form.is_valid() and report_form.is_valid():
#                 fundraiser = fundraiser_form.save(commit=False)
#                 fundraiser.user = request.user  # Assuming the user is logged in
#                 fundraiser.save()
#                 requisites = requisites_form.save()
#                 report = report_form.save(commit=False)
#                 report.donation_target = fundraiser
#                 report.save()
#                 return redirect('success_url')  # Redirect to success page
#         else:
#             fundraiser_form = FundraiserForm()
#             requisites_form = DonationRequisitesForm()
#             report_form = DonationTargetReportForm()
#         return render(request, 'fundraiser_form.html',
#                       {'fundraiser_form': fundraiser_form, 'requisites_form': requisites_form,
#                        'report_form': report_form})