from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email