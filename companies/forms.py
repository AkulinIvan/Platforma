from django import forms
from companies.models import Companies
from .models import Cities
from django.contrib.auth.models import User


class CompanyForm(forms.ModelForm):
    name = forms.TextInput()
    city = forms.ModelChoiceField(queryset=Cities.objects.all(), empty_label="Город не выбран", required=False, label="Город")
    phone_number = forms.TextInput()
    mail = forms.TextInput()
    info = forms.Textarea()
    sms_master = forms.BooleanField()
    sms_worker = forms.BooleanField()
    status = forms.BooleanField()
    
    class Meta:
        model = Companies
        fields = ['name', 'city', 'phone_number', 'mail', 'info', 'sms_master', 'sms_worker', 'status']
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "city": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "mail": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }),
            "info": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Информация о компании'
            })
            # "sms_master": forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Смс  мастеру:'
            # }),
            # "sms_worker": forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Смс исполнителю:'
            # }),
            # "status": forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Статус компании'
            # })
        
        }
    