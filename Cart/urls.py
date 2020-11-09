from django.urls import path
from . import views

urlpatterns = [
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('confirm/', views.confirm, name='confirm'),
    path('', views.cart, name='cart'),
]