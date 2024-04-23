from django.contrib.auth.models import User
from django.db import models

# Модель Соціальних спільнот, або людини, яка відкриває збір

class SocialCommunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='communities')
    avatar = models.ImageField

    def __str__(self):
        return self.name

#Модель Грантів

class Grant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

#Модель Донатів

class Donation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Модель тегів по яким будуть розроблені фільтри

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Модель людей які будуть донатити

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField('Tag', related_name='users')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username

#Модель організацій які надають гранти

class GrantOrg(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
