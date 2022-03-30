from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
	slug = models.SlugField(null = True, unique = True, db_index = True)
	name = models.CharField(max_length=30, verbose_name="Название")
	image = models.ImageField(upload_to="c_img/", null=True, verbose_name="Изображение")

	def _str_(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse('category_page', kwargs = {'slug': self.slug})	

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	
	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"


class Product(models.Model):
	slug = models.SlugField(null = True, unique = True, db_index = True)
	name = models.CharField(max_length=50, verbose_name="Название", null = 'Something')
	price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	image = models.ImageField(upload_to="p_img/", null=True)
	description = models.TextField(null=True)

	def _str_(self):
		return f'{self.name}'

	def get_absolute_url(self):
		return reverse('product_detail', kwargs = {'category_slug': self.category.slug, 'product_slug': self.slug})	

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	
	class Meta:
		verbose_name = "Блюдо"
		verbose_name_plural = "Блюда"