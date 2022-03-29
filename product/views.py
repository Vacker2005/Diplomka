from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, "index.html", context)


def categories(request):
	categories = Category.objects.all()

	context = {
		'categories': categories
	}

	return render(request, "categories.html", context)


def category_product(request, slug):
	category = get_object_or_404(Category, slug=slug)
	products = Category.objects.get(slug=slug).product_set.all()

	context = {
		'products':products,
		'category': category,
	}

	return render(request, "products.html", context)

def product_detail(request, category_slug, product_slug):
	category = get_object_or_404(Category, slug=category_slug)
	product = get_object_or_404(Product, slug=product_slug)

	context = {
		'product': product,
		'category': category,
	}

	return render(request, "product_detail.html", context)