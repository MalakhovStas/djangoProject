"""Модуль описывающий формы приложения"""
from django import forms


class AddProductForm(forms.Form):
    """Форма добавления продукта"""
    title = forms.CharField(label='Название', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea())
    price = forms.DecimalField(label='Цена', min_value=1)
