from django.shortcuts import render
from django.views import generic

from .models import Category, Subcategory, Product


class IndexView(generic.ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        return Product.objects.order_by('-id')[:10]


class CategoryListView(generic.ListView):
    model = Category


class SubcategoryDetailView(generic.DetailView):
    model = Subcategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(subcategory=context['object'])
        return context

class ProductDetailView(generic.DetailView):
    model = Product