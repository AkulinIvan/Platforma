from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    
    # def save(self, commit=True):
    #     form = super().save(commit=False)
    #     if commit:
    #         form.save() 
    #     return form   
