from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer


# Create your views here.

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to a view that shows the list of customers
    else:
        form = CustomerForm()
    return render(request, "customer/customer_form.html", {"form": form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer/customer_list.html", {"customers": customers})