"""Модуль описывающий модели приложения"""
from django.db import models


class Product(models.Model):
    """Класс описывающий модель Product"""
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(
        max_digits=14,
        decimal_places=0,
        verbose_name='цена',
    )
