from django import forms

class GrantFilterForm(forms.Form):
    search = forms.CharField(required=False, label='Поиск')
