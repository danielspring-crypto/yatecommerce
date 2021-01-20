from django.contrib import admin
from .models import Person, Product, Category, Brand, Color, Size, MainBanner, BrandBanner, EventBanner, BrandBanner2, About, Help, Term, Contact
from django.contrib.auth.models import Group
import datetime
from django.http import HttpResponse
from django.urls import reverse
import csv

admin.site.unregister(Group)

admin.site.site_header = '(ရိပ်) Yate Ecommerce'
admin.site.index_title = 'Adminsitration Panel'
admin.site.site_title = 'ရိပ်'

admin.site.register(MainBanner)
admin.site.register(BrandBanner)
admin.site.register(EventBanner)
admin.site.register(BrandBanner2)

admin.site.register(About)
admin.site.register(Help)
admin.site.register(Term)
admin.site.register(Contact)

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	actions = [export_to_csv]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	actions = [export_to_csv]

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	actions = [export_to_csv]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	actions = [export_to_csv]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}
	actions = [export_to_csv]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated', 'person']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}
	actions = [export_to_csv]
