from datetime import datetime

from django import forms

from .models import Articles

from django.core.validators import ValidationError


class ArticlesForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street'].empty_label = 'Выберите улицу'
        self.fields['house'].empty_label = 'Выберите номер дома'
        self.fields['view'].empty_label = 'Выберите вид заявки'
        self.fields['type'].empty_label = 'Выберите тип заявки'
        self.fields['company'].empty_label = 'Выберите компанию'
        self.fields['master'].empty_label = 'Выберите мастера'
        self.fields['worker'].empty_label = 'Выберите исполнителя'
        
    class Meta:
        model = Articles
        fields = ['create_time', 'fio', 'phone', 'text', 'street', 'house', 'flat', 'materials', 'files', 'comment', 'view', 
                'type', 'company', 'master', 'worker']
        

        widgets = {
            "create_time": forms.DateTimeInput(attrs={
                'class': 'form-control'
            }),
            "fio": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО', 
                }),
            "phone": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заявки'
                
            }),
            "street": forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Улица'
            }),
            "house": forms.Select(attrs={
                'class': 'form-control'
            }),
            "flat": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Квартира'
            }),
            "materials": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Материалы'
            }),
            "files": forms.FileInput(attrs={
                'class': 'form-control'
            }),
            "comment": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "view": forms.Select(attrs={
                'class': 'form-control'
            }),
            "type": forms.Select(attrs={
                'class': 'form-control'
            }),
            "company": forms.Select(attrs={
                'class': 'form-control'
            }),
            "master": forms.Select(attrs={
                'class': 'form-control'
            }),
            "worker": forms.Select(attrs={
                'class': 'form-control'
            })
    }
        
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
        
    # def clean_fio(self):
    #     fio = self.cleaned_data['fio']
    #     if not fio:
    #         raise forms.ValidationError('Поле "ФИО заявителя" не может быть пустым')
    #     return fio  
    
    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     if not text:
    #         raise forms.ValidationError('Поле "Текст заявки" не может быть пустым')
    #     return text
    
    # def clean_street(self):
    #     street = self.cleaned_data['street']
    #     if not street:
    #         raise forms.ValidationError('Поле "Улица" не может быть пустым')
    #     return street
    
    # def clean_house(self):
    #     house = self.cleaned_data['house']
    #     if not house:
    #         raise forms.ValidationError('Поле "Дом" не может быть пустым')
    #     return house
    
    # def clean_view(self):
    #     view = self.cleaned_data['view']
    #     if not view:
    #         raise forms.ValidationError('Поле "Вид заявки" не может быть пустым')
    #     return view 
        
    # def clean_type(self):
    #     type = self.cleaned_data['type']
    #     if not type:
    #         raise forms.ValidationError('Поле "Тип заявки" не может быть пустым')
    #     return type
    
        


