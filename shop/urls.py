from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('category/', views.CategoryListView.as_view(), name='category_list'),

    path('subcategory/detail/<slug:slug>', views.SubcategoryDetailView.as_view(), name='subcategory_detail'),

    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]
