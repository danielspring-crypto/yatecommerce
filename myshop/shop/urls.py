from django.urls import path 
from .import views 

app_name = 'shop'

urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('product/search/', views.search, name='search'),
	path('tag/<slug:tag_slug>/', views.product_list, name='product_list_by_tag'),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]