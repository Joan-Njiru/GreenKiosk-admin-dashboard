from django.urls import path
from . import views

urlpatterns = [
    path('make-payment/', views.make_payment, name='make_payment'),
    path('receipt/', views.receipt_note, name='receipt_note'),
]
