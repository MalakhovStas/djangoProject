"""Модуль описывающий логику отображений приложения"""
from django.views.generic import ListView

from .forms import AddProductForm
from .models import Product


class ProductListView(ListView):
    """Представление для отображения списка товаров"""
    template_name = 'index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        """Для добавления формы в контекст"""
        context = super().get_context_data(*args, **kwargs)
        context['form'] = AddProductForm()
        return context

    def post(self, request, *args, **kwargs):
        """Логика обработки post запроса добавления продукта"""
        form = AddProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
            )
        return self.get(request)
