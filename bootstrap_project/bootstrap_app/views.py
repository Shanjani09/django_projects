from django.shortcuts import render
from .models import Product  
from django.http import HttpResponse
def product_list(request):
    products = Product.objects.all() 
    return render(request, 'product.html', {'products': products}) 
def add_product(request):
    product1 = Product(name="iPhone 15", description="Latest Apple smartphone with A16 Bionic chip", price=999.99)
    product2 = Product(name="Samsung Galaxy S23", description="Flagship Samsung phone with great camera", price=899.99)
    product3 = Product(name="Sony WH-1000XM5", description="Noise-canceling wireless headphones", price=399.99)
    product1.save()
    product2.save()
    product3.save()
    return HttpResponse("Products added successfully!")
def delete_products(request):
    Product.objects.all().delete()  
    return HttpResponse("All products have been deleted.")
def carousel_view(request):
    return render(request, 'carousel.html') 
def grid_view(request):
    return render(request, 'grid.html')
