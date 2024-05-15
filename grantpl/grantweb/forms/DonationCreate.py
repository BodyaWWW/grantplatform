from django import forms

from grantpl.grantweb.models.DonationTargetStatus import DonationTarget, DonationRequisites, DonationTargetReport


class FundraiserForm(forms.ModelForm):
    class Meta:
        model = DonationTarget
        fields = ['title', 'description', 'report_expected_due_date']

class DonationRequisitesForm(forms.ModelForm):
    class Meta:
        model = DonationRequisites
        fields = ['requisites_monobank_jar', 'requisites_iban', 'requisites_paypal']

class DonationTargetReportForm(forms.ModelForm):
    class Meta:
        model = DonationTargetReport
        fields = ['report', 'files']