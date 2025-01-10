from rest_framework import serializers
from .models import *

# Serializer for MainCategory
class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'

class CategoryPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPDF
        fields = ['id', 'category', 'pdf_type', 'pdf_file']  # Include the necessary fields

# Serializer for CategoryImage
class CategoryImageSerializer(serializers.ModelSerializer):
    category = MainCategorySerializer()  # Optional: Nested representation of MainCategory

    class Meta:
        model = CategoryImage
        fields = '__all__'

# Serializer for Manufacturer
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

# Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    category = MainCategorySerializer()  # Optional: Nested representation of MainCategory

    class Meta:
        model = Product
        fields = '__all__'

# Serializer for ProductManufacturer
class ProductManufacturerSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Optional: Nested representation of Product
    manufacturer = ManufacturerSerializer()  # Optional: Nested representation of Manufacturer

    class Meta:
        model = ProductManufacturer
        fields = '__all__'

# Serializer for Headings
class HeadingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headings
        fields = '__all__'

# Serializer for HeadingsDetails
class HeadingsDetailsSerializer(serializers.ModelSerializer):
    heading = HeadingsSerializer()  # Optional: Nested representation of Headings
    category = MainCategorySerializer()  # Optional: Nested representation of MainCategory

    class Meta:
        model = HeadingsDetails
        fields = '__all__'
