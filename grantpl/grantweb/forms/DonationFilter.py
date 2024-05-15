from django import forms
class DonationTargetFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'Все'),
        ('В ОБЗОРЕ', 'В ОБЗОРЕ'),
        ('АКТИВНЫЙ', 'АКТИВНЫЙ'),
        ('ОТКЛОНЕННЫЙ', 'ОТКЛОНЕННЫЙ'),
        ('ЗАВЕРШЕННЫЙ', 'ЗАВЕРШЕННЫЙ'),
        ('ЗАВЕРШЕНО И ПОДТВЕРЖДЕНО', 'ЗАВЕРШЕНО И ПОДТВЕРЖДЕНО'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)