from django.db import models

from grantpl.grantweb.models.User import User


class DonationTarget(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    report_expected_due_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_requisites = models.ForeignKey('DonationRequisites', on_delete=models.CASCADE)
    donation_target_status = models.ForeignKey('DonationTargetStatus', on_delete=models.CASCADE)
    donation_target_report = models.ForeignKey('DonationTargetReport', on_delete=models.CASCADE)

class DonationTargetStatus(models.Model):
    status = models.CharField(max_length=255)

class DonationRequisites(models.Model):
    requisites_monobank_jar = models.CharField(max_length=255)
    requisites_iban = models.CharField(max_length=255)
    requisites_paypal = models.CharField(max_length=255)

class DonationTargetReport(models.Model):
    report = models.TextField()
    files = models.BinaryField(null=True)
    donation_target = models.ForeignKey(DonationTarget, on_delete=models.CASCADE)

class Grant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    source_url = models.CharField(max_length=255)
    completed_at = models.DateTimeField(null=True)