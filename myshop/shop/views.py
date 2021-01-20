from django.shortcuts import render, get_object_or_404
from .models import Person, Product, Category, Brand, Color, Size, MainBanner, BrandBanner, EventBanner, BrandBanner2, About, Help, Term, Contact
from cart.forms import CartAddProductForm
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q

def contact(request):
	if request.method == 'POST':
	    name = request.POST['name']
	    email = request.POST['email']
	    content = request.POST['content']
	    print(name, email, content)
	    contact = Contact(name=name, email=email, content=content)
	    contact.save()
	return render(request, 'shop/contact.html')


def about(request):
    about = About.objects.all()
    return render(request, "shop/about.html", {'about':about})

def help(request):
    help = Help.objects.all()
    return render(request, "shop/help.html", {'help':help})

def term(request):
    term = Term.objects.all()
    return render(request, "shop/term.html", {'term':term})

def search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(Q(name__icontains=query) | Q(brand_type__icontains=query)).order_by('-created')
	people = Person.objects.filter(Q(name__icontains=query))
	category = Category.objects.filter(Q(name__icontains=query))
	brand = Brand.objects.filter(Q(name__icontains=query))
	color = Color.objects.filter(Q(name__icontains=query))
	size = Size.objects.filter(Q(name__icontains=query))
	context = {
		'products':products,
		'people':people,
		'category':category,
		'brand':brand,
		'color':color,
		'size':size,
	}
	return render(request, "shop/product/list.html", context)

def product_list(request, person_slug=None, tag_slug=None, category_slug=None):
	person = None
	people = Person.objects.all()
	products = Product.objects.order_by('-created')
	category = None
	categories = Category.objects.all()
	covers1 = MainBanner.objects.all()
	covers2 = BrandBanner.objects.all()
	covers3 = EventBanner.objects.all()
	covers4 = BrandBanner2.objects.all()
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		products = products.filter(tags__in=[tag])
	if person_slug:
		person = get_object_or_404(Person, slug=person_slug)
		products = products.filter(person=person)
	if category_slug:
	    category = get_object_or_404(Category, slug=category_slug)
	    categories = categories.filter(category=category)
	return render(request, 'shop/product/list.html', {'person': person, 'people': people, 'products': products, 'tag': tag, 'category':category, 'categories':categories, 'covers1':covers1, 'covers2':covers2, 'covers3':covers3, 'covers4':covers4})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	product_tags_ids = product.tags.values_list('id', flat=True)
	similar_products = Product.objects.filter(tags__in=product_tags_ids).exclude(id=product.id)
	similar_products = similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags')[:5]
	cart_product_form = CartAddProductForm()
	return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form, 'similar_products': similar_products})

