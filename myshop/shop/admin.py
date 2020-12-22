from django.contrib import admin
from .models import Person, Product, Category, Brand, Color, Size 

admin.site.site_header = '(ရိပ်) Yate Ecommerce'                    
admin.site.index_title = 'Adminsitration Panel'                  
admin.site.site_title = 'ရိပ်' 

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}
