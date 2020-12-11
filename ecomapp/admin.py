from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
class ProductAdmin(ImportExportModelAdmin):
    resource_class = Product

from import_export import resources
from .models import Product

from import_export.admin import ImportExportActionModelAdmin

class BookAdmin(ImportExportActionModelAdmin):
    model = Product

admin.site.register(Product,BookAdmin)

admin.site.register(
    [Admin, Customer, Category, Cart, CartProduct, Order, ProductImage])
