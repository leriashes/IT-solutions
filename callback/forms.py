from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['first_name', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Имя',
            'phone': 'Телефон',
        }
    
    agree_to_privacy_policy = forms.BooleanField(
        label='Я согласен с политикой конфиденциальности',
        required=True,
        widget=forms.CheckboxInput
    )
