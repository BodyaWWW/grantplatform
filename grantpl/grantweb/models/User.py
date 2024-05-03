from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(null=True)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

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


