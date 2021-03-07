from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_name = models.CharField(max_length=50, null=True, help_text='Введите свою фамилию. Максимальное кол-во символов 50.')
    first_name = models.CharField(max_length=50, null=True, help_text='Введите своё имя. Максимальное кол-во символов 50.')
    patronymic = models.CharField(max_length=50, null=True, help_text='Введите отчество. Максимальное кол-во символов 50.')
    email = models.EmailField(max_length=254, null=True, unique=True, help_text='Введите почту.')
    description = models.CharField(max_length=254, null=True, help_text='Информация о себе')
    profile_pic = models.ImageField(null=True, blank=True, default='img-cat.png', upload_to='profile_pics/')
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email