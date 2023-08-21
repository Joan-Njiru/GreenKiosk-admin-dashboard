from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('view_cart/', views.view_cart, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]
