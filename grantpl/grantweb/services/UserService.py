from grantweb.models.CustomUser import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

def check_existing_user(email):

    try:
        user = CustomUser.objects.get(email=email)
        return True
    except CustomUser.DoesNotExist:
        return False


def validate_login(email, password):
    user = authenticate(email=email, password=password)
    if user is None:
        raise ValidationError("Invalid email or password.")