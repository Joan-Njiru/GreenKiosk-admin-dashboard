from django.shortcuts import render
from inventory.models import Product
from .forms import ProductUploadForm
from django.shortcuts import redirect


def upload_product(request):
    if request.method == 'POST':
        upload_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.FILES)  # Use request.FILES
        if form.is_valid():
            form.save()
            # return redirect('products_list_view')

    else:
        form = ProductUploadForm()

    return render(request, "inventory/product_upload.html", {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request,"inventory/products_list.html",{"products":products})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",
                  {"product":product})

def cart_view(request):
    cart_items = []
    return render(request, 'inventory/cart.html', {'cart_items': cart_items})

def edit_product_view(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail_view", id=product.id)
    else:
        form = ProductUploadForm(instance=product) 

    return render(request, "inventory/edit_product.html", {"form": form})

    

