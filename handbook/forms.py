from django import forms
from django.forms import ModelForm

from companies.models import Companies, PublishedManager
from .models import House, Master, Street, Worker, City, Roles
from django.contrib.auth.models import User


class MasterForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class WorkerForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class Dezh_WorkerForm(forms.ModelForm):
    name = forms.TextInput()
    
    
class WorkersForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    master = forms.ModelChoiceField(queryset=Master.published.all(), empty_label="Мастер не выбран", required=False, label="Мастер")
    
                    


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
        
class AddMasterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'Введите имя'
        self.fields['phone_number'].empty_label = 'Введите номер телефона'
        # self.fields['company'].empty_label = 'Введите номер телефона'
        self.fields['user'].empty_label = 'Выберите аккаунт'
    
    class Meta:
        model = Worker
        fields = ['name', 'phone_number', 'company', 'user'] 
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя мастера'
            }),
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            # "company": forms.Select(attrs={
            #     'class': 'form-control'                
            # }),
            "user": forms.Select(attrs={
                'class': 'form-control'
            })
        }
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data
        

    
class AddWorkerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].empty_label = 'Введите имя'
        self.fields['type_worker'].empty_label = 'Выберите тип заявок'
        # self.fields['sms'].empty_label = 'Выберите статус смс'
        self.fields['phone_number'].empty_label = 'Введите номер телефона'
        # self.fields['company'].empty_label = 'Выберите компанию'
        self.fields['user'].empty_label = 'Выберите аккаунт исполнителя'
        
    class Meta:
        model = Worker
        fields = ['name', 'type_worker', 'phone_number', 'user'] 
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя работника'
            }),
            "type_worker": forms.Select(attrs={
                'class': 'form-control'
            }),
            "phone_number": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            # "company": forms.Select(attrs={
            #     'class': 'form-control'
            # }),
            # "sms": forms.BooleanField(attrs={
            #     'class': 'form-control'
            # }),
            "user": forms.Select(attrs={
                'class': 'form-control'
            })
        }
        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data
        
class HouseForm(forms.ModelForm):
    name = forms.TextInput()
    street = forms.ModelChoiceField(queryset=Street.objects.all(), empty_label="Улица не выбрана", required=False, label="Улица")
    company = forms.ModelChoiceField(queryset=Companies.published.all(), empty_label="Компания не выбрана", required=False, label="Компания")
    master = forms.ModelChoiceField(queryset=Master.published.all(), empty_label="Мастер не выбран", required=False, label="Мастер")
    status = forms.BooleanField()
    plumbing = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Сантехник не выбран", required=False, label="Сантехник")
    electrician = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Электрик не выбран", required=False, label="Электрик")
    carpenter = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    cleaners = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    wipers = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    improvement = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    plumber_certificate = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    electrician_certificate = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    networks = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    act = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    deratization = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    pest_control = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    disinfection = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    verification_of_meters = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    SOI_inspection = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    passport = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    intercom_ROST = forms.ModelChoiceField(queryset=Worker.published.all(), empty_label="Исполнитель не выбран", required=False, label="Исполнитель")
    
    
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


