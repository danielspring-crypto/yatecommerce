from django.urls import path
from .import views

app_name = 'shop'

urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('product/search/', views.search, name='search'),
	path('about/', views.about, name='about'),
	path('help/', views.help, name='help'),
	path('term/', views.term, name='term'),
	path('contact/', views.contact, name='contact'),
	path('tag/<slug:tag_slug>/', views.product_list, name='product_list_by_tag'),
	path('<slug:person_slug>/', views.product_list, name='product_list_by_people'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]