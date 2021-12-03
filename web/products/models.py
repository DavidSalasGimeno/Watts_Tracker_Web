from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name='Category'
	def __str__(self):
		return self.name

class Product(models.Model):
	title = models.CharField(max_length=50)
	categories = models.ForeignKey(Category, on_delete=models.CASCADE)
	img = models.CharField(max_length=400)
	efficiencyImg = models.CharField(max_length=400)
	pirce = models.FloatField()
	discount = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name='Product'

	def __str__(self):
		return self.title