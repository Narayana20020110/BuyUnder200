from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import CustomerForm

def homepage(request):
    products = Product.objects.all()
    return render(request, 'homepage.html', {'products': products})

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.product = product
            customer.save()
            return redirect('homepage')
    else:
        form = CustomerForm()

    return render(request, 'buy_product.html', {'form': form, 'product': product})