from django.shortcuts import render, redirect
from .forms import CartForm
from .models import Cart
from inventory.models import Product
from orders.models import Orders

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_payment = sum(item.payment for item in cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items, 'total_payment': total_payment})

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.product_order = Orders.objects.create(order_status='cart')  # Assuming 'order_status' is a field in Orders model
            cart_item.user = request.user
            cart_item.product = product
            cart_item.payment = product.price * cart_item.number_of_items
            cart_item.save()
            return redirect('view_cart')
    else:
        form = CartForm()
    
    return render(request, 'cart/add_to_cart.html', {'product': product, 'form': form})
