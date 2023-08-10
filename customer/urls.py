from django.urls import path
from . import views

app_name = 'customer'  # Replace 'your_app_name' with the name of your app

urlpatterns = [
    path('add_customer/', views.add_customer, name='add_customer'),
    path('customer_list/', views.customer_list, name='customer_list'),
]