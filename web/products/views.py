from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def products(request):
	products = Product.objects.all()
	categories = Category.objects.all()

	return render(request, 'products.html', {'products':products[0],'categories':categories})

