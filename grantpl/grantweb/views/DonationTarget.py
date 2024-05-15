# views.py
from django.shortcuts import render, redirect

from ..forms.DonationFilter import DonationTargetFilterForm
from ..forms.forms import DonationTargetForm  # Проверьте путь к вашей форме
from ..models.models import DonationTarget  # Проверьте путь к вашей модели
from django.views.generic import TemplateView

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

class DonationCreate(TemplateView):

    template_name = 'donation_create.html'

    def create_fundraiser(request):
        if request.method == 'POST':
            fundraiser_form = FundraiserForm(request.POST)
            requisites_form = DonationRequisitesForm(request.POST)
            report_form = DonationTargetReportForm(request.POST, request.FILES)
            if fundraiser_form.is_valid() and requisites_form.is_valid() and report_form.is_valid():
                fundraiser = fundraiser_form.save(commit=False)
                fundraiser.user = request.user  # Assuming the user is logged in
                fundraiser.save()
                requisites = requisites_form.save()
                report = report_form.save(commit=False)
                report.donation_target = fundraiser
                report.save()
                return redirect('success_url')  # Redirect to success page
        else:
            fundraiser_form = FundraiserForm()
            requisites_form = DonationRequisitesForm()
            report_form = DonationTargetReportForm()
        return render(request, 'fundraiser_form.html',
                      {'fundraiser_form': fundraiser_form, 'requisites_form': requisites_form,
                       'report_form': report_form})