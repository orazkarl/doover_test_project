from django.urls import path, include

from . import views

urlpatterns = [
    path('checkout/', views.order_checkout, name='order_checkout'),
    path('', views.OrderListView.as_view(), name='order_list'),
]
