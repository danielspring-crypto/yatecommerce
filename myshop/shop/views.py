from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q

def search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(Q(slug__icontains=query) | Q(name__icontains=query) | Q(tags__name__icontains=query)).order_by('-created')
	categories = Category.objects.filter(Q(name__icontains=query))
	context = {
		'products':products,
		'categories':categories
	}
	return render(request, "shop/product/list.html", context)

def product_list(request, category_slug=None, tag_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		products = products.filter(tags__in=[tag])
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'products': products, 'tag': tag})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	product_tags_ids = product.tags.values_list('id', flat=True)
	similar_products = Product.objects.filter(tags__in=product_tags_ids).exclude(id=product.id)
	similar_products = similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags')[:5]
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'similar_products': similar_products})

