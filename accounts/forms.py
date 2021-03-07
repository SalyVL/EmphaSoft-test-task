from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CustomUserCreationForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput)
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(None)
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'description', 'profile_pic')
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'patronymic': forms.TextInput(attrs={'placeholder': 'Отчество'}),
            'email': forms.TextInput(attrs={'placeholder': 'Почтовый ящик'}),
            'description': forms.TextInput(attrs={'placeholder': 'Информация о себе'}),
        }
        error_messages = {
            'first_name': {'required':'Введите имя', 'max_length':'Слишком много символов'},
            'last_name': {'required': 'Введите фамилию', 'max_length':'Слишком много символов'},
            'patronymic': {'required': 'Введите Отчество', 'max_length':'Слишком много символов'},
            'description': {'required': 'Введите информацию о себе', 'max_length':'Слишком много символов'},
            'email': {'required': 'Введите почтовый ящик', 'invalid':'Поле заполнено некорректно', 'unique': 'Данный почтовый ящик уже зарегистрирован'}
        }