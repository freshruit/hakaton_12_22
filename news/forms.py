from .models import Applications
from django.forms import ModelForm, TextInput, Textarea


class ApplicationsForm(ModelForm):
    class Meta:
        model = Applications
        fields = ['lastname', 'firstname', 'thirdname', 'job', 'placejob',
                  'theme', 'header', 'full_text']

        widgets = {
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "firstname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "thirdname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "job": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "placejob": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место работы'
            }),
            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "header": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Оглавление'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }


