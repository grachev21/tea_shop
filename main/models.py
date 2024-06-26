from django.db import models
from users.models import CustomUser 

'''
загаловок
категория
артикул
наличие
характеристики
фотография
описание
'''

class Category(models.Model):
    catigory = models.CharField(max_length=100, verbose_name='Категория')

class AvailabilityStatus(models.Model):
    availability = models.CharField(max_length=100, verbose_name='Наличие')
    
class Goods(models.Model):
    title = models.CharField(max_length=100, verbose_name='Загловок')
    vendor_code  = models.CharField(max_length=100, verbose_name='Артикул')
    availability = models.ForeignKey(AvailabilityStatus, on_delete=models.CASCADE, verbose_name='Категория')
    characteristic = models.CharField(max_length=100, verbose_name='Характеристика')
    photo = models.CharField(max_length=100, verbose_name='Фотографии')
    description = models.TextField(verbose_name='Описание')
    category  = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')


class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Ползователь')
    vendor_code  = models.CharField(max_length=100, verbose_name='Артикул')

