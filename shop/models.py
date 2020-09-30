from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='subcategory')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.DO_NOTHING, related_name='product')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, db_index=True, unique=True)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
