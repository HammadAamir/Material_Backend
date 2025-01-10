from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib import admin
from .models import Manufacturer, Product, ProductManufacturer

from django.contrib import admin
from .models import Manufacturer, Product, ProductManufacturer

# Define ProductManufacturer Inline
class ProductManufacturerInline(admin.TabularInline):
    model = ProductManufacturer  # Use the intermediary table as the inline
    extra = 1  # Number of empty rows to show for adding new links

    # Display fields for creating products
    fields = ['product']  # This lets you select or create a product\

    autocomplete_fields = ['product']  # Enable autocomplete for Product selection (optional)

# Customize Manufacturer Admin
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']  # Display manufacturer name
    inlines = [ProductManufacturerInline]  # Link to the intermediary inline

# Register Manufacturer Admin
admin.site.register(Manufacturer, ManufacturerAdmin)

# # Optional: Add Product to the admin (for standalone management)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['Type', 'Kurztext', 'category']
    search_fields = ['Type', 'Kurztext']


admin.site.register(MainCategory)
admin.site.register(CategoryImage)
# admin.site.register(Manufacturer)
# admin.site.register(Product)
admin.site.register(ProductManufacturer)
admin.site.register(Headings)
admin.site.register(HeadingsDetails)
admin.site.register(CategoryPDF)
