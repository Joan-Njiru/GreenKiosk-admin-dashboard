from django.urls import path
from .views import cart_view, edit_product_view, product_detail, product_list, upload_product


urlpatterns = [
    path("products/upload",upload_product,name="product_upload_view"),
    path("products/list",product_list,name='products_list_view'),
    path("products/<int:id>/",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>/",edit_product_view,name="product_edit_view"),
    path('cart/',cart_view, name='cart'),

]
  
