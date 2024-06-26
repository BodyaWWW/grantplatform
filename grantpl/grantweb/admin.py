from django.contrib import admin


# Регистрация моделей в административной панели
from .models.models import CustomUser,User,Role
from .models.models import DonationRequisites, DonationTarget, DonationTargetStatus, \
    Grant, DonationTargetReport

admin.site.register(CustomUser)
admin.site.register(DonationRequisites)
admin.site.register(DonationTarget)
admin.site.register(DonationTargetStatus)
admin.site.register(Grant)
admin.site.register(DonationTargetReport)
admin.site.register(User)
admin.site.register(Role)