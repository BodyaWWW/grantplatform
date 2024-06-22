from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(null=True)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return f"User(email={self.email}, password={self.password})"
class UserProfile(models.Model):
    profile_photo = models.BinaryField(null=True)
    description = models.TextField()
    messenger = models.ForeignKey('Messenger', on_delete=models.CASCADE)

class Messenger(models.Model):
    name = models.CharField(max_length=255)
    actual_id = models.CharField(max_length=255)

class UserType(models.Model):
    type = models.CharField(max_length=255)

class Role(models.Model):
    role = models.CharField(max_length=255)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    ACCOUNT_TYPE_CHOICES = (
        ('personal', 'Личный'),
        ('organizational', 'Организационный'),
    )

    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES)
    password = models.CharField(max_length=255)
    account_creation_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    last_login_time = models.DateTimeField(null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)

    # objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __init__(self, email, account_type, password, company_name=None, company_website=None):
        # super().__init__(*args, **kwargs)
        self.email = email
        self.account_type = account_type
        self.password = password
        self.company_name = company_name
        self.company_website = company_website

    def __str__(self):
        return self.email



class DonationTarget(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    report_expected_due_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    donation_requisites = models.ForeignKey('DonationRequisites', on_delete=models.CASCADE, null=True, default=None)
    donation_target_status = models.ForeignKey('DonationTargetStatus', on_delete=models.CASCADE)
    donation_target_report = models.ForeignKey('DonationTargetReport', on_delete=models.CASCADE, null=True,default=None)

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
