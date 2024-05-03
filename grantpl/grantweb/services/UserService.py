from grantweb.models.CustomUser import CustomUser

def check_existing_user(email):

    try:
        user = CustomUser.objects.get(email=email)
        return True
    except CustomUser.DoesNotExist:
        return False