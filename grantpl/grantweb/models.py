from django.contrib.auth.models import User
from django.db import models

class SocialCommunity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='communities')

    def __str__(self):
        return self.name

class Grant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField('Tag', related_name='users')

    def __str__(self):
        return self.user.username
