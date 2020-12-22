from django.db import models
from django.urls import reverse 
from taggit.managers import TaggableManager


class Person(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'person'
		verbose_name_plural = 'people'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list_by_people', args=[self.slug])


class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])

class Brand(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'brand'
		verbose_name_plural = 'brands'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list_by_brand', args=[self.slug])

class Color(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'color'
		verbose_name_plural = 'colors'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list_by_color', args=[self.slug])

class Size(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'size'
		verbose_name_plural = 'sizes'

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_list_by_size', args=[self.slug])


class Product(models.Model):
	person = models.ForeignKey(Person, related_name='products', on_delete=models.CASCADE)
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
	color = models.ForeignKey(Color, related_name='products', on_delete=models.CASCADE)
	size = models.ForeignKey(Size, related_name='products', on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	tags = TaggableManager()	
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])