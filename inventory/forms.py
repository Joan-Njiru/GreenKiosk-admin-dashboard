from django import forms
from .models import Product

# class ProductUploadForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"


class ProductUploadForm(forms.ModelForm):
    vendor_id = forms.IntegerField()  # Add the vendor_id field
    stock = forms.IntegerField()  # Add the stock field

    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'vendor_id','stock']