from django.contrib import admin

# Register your models here.
from .models import Product, Category
class ProductAdmin(admin.ModelAdmin):
	readonly_fields=('created','updated')


class CategoryAdmin(admin.ModelAdmin):
	readonly_fields=('created','updated')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
