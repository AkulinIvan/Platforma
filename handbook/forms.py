from django import forms
from django.forms import ModelForm
from .models import Company, House, Master, Street, Worker, City, Roles
from django.contrib.auth.models import User


class MasterForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class WorkerForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class Dezh_WorkerForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class WorkersForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    master = forms.ModelChoiceField(queryset=Master.objects.all(), empty_label="Мастер не выбран", required=False, label="Мастер")
    
                    
class CompanyForm(forms.ModelForm):
    name = forms.TextInput()
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Город не выбран", required=False, label="Город")
    phone_number = forms.TextInput()
    mail = forms.TextInput()
    info = forms.Textarea()
    sms_master = forms.BooleanField()
    sms_worker = forms.BooleanField()
    status = forms.BooleanField()
    
    class Meta:
        model = Company
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
    

class CityForm(forms.ModelForm):
    name = forms.TextInput()
    status = forms.BooleanField()

    

class StreetForm(forms.ModelForm):
    name = forms.TextInput()
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="Город не выбран", required=False, label="Город")
    status = forms.BooleanField()

    class Meta:
        model = Street
        fields = ['name', 'city', 'status']
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "city": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            })
        }

class UsernamesForm(forms.ModelForm):
    name = forms.TextInput()
    phone_number = forms.TextInput()
    mail = forms.TextInput()
    role = forms.ModelChoiceField(queryset=Roles.objects.all(), empty_label="Роль не выбрана", required=False, label="Роль")
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Компания не выбрана", required=False, label="Компания")
    ATS = forms.TextInput()
    sms = forms.TextInput()
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Пользователь не выбран", required=False, label="Пользователь")

        
class HouseForm(forms.ModelForm):
    name = forms.TextInput()
    street = forms.ModelChoiceField(queryset=Street.objects.all(), empty_label="Улица не выбрана", required=False, label="Улица")
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="Компания не выбрана", required=False, label="Компания")
    master = forms.ModelChoiceField(queryset=Master.objects.all(), empty_label="Мастер не выбран", required=False, label="Мастер")
    status = forms.BooleanField()
    plumbing = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    electrician = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    carpenter = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    cleaners = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    wipers = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    improvement = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    plumber_certificate = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    electrician_certificate = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    networks = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    act = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    deratization = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    pest_control = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    disinfection = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    verification_of_meters = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    SOI_inspection = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    passport = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    intercom_ROST = forms.ModelChoiceField(queryset=Worker.objects.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")

    class Meta:
        model = House
        fields = ['name', 'street', 'company',]
        # widgets = {
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "name": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Название'
        #     }),
        #     "city": forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     }),
        #     "status": forms.BooleanField(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Статус'
        #     })
        # }

        
# class CompanyForm(ModelForm):
#     class Meta:
#         model = Company
#         fields = ['name', 'phone_number', 'mail', 'city', 'info', 'sms_master', 'sms_worker', 'status']
#         widgets = {
#             "name": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Название компании'
#             }),
#             "phone_number": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Номер телефона'
#             }),
#             "mail": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Е-майл'
#             }),
#             "city": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Город'
#             }),
#             "info": forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Информация'
#             }),
#             "sms_master": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Смс мастеру'
#             }),
#             "sms_executor": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Смс исполнителю'
#             }),
#             "status": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Статус'
#             }),
            
#         }


