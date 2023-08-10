from django.shortcuts import get_object_or_404, render
from payment.models import Payment
from .forms import PaymentForm

def make_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Save the data to the database
            form.save()

            # Prepare the context for the receipt template
            context = {
                'receipt_number': form.instance.receipt,
                'payment_status': form.cleaned_data['payment_status'],
                'payment_amount': form.cleaned_data['amount'],
                'payment_date_time': form.cleaned_data['payment_date_time'],
                'payment_method': form.cleaned_data['payment_method'],
                # Add more fields as needed from the Payment model
            }

            # Render the receipt template with the context data
            return render(request, "payment/payment_success.html", context)
    else:
        form = PaymentForm()

    return render(request, "payment/payment_form.html", {"form": form})

def receipt_note(request):
    if request.method == "GET":
        receipt_number = request.GET.get('receipt_number')
        if receipt_number:
            payment = get_object_or_404(Payment, receipt=receipt_number)
            # Now you have the payment object with all the payment details
            # Return the payment object as context data to be rendered in the receipt_note template
            return render(request, "payment/receipt_note.html", {'payment': payment})

    return render(request, "payment/receipt_note.html", {})
