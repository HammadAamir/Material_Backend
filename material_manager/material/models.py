from django.db import models

# Main Category
class MainCategory(models.Model):
    categoryID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CategoryPDF(models.Model):
    PDF_TYPE_CHOICES = [
        ('datenblatter', 'Datenblatter'),
        ('montageanleitung', 'Montageanleitung'),
        ('prufzertifikate', 'Prufzertifikate'),
        ('sonstiges', 'Sonstiges'),
    ]

    id = models.AutoField(primary_key=True)  # Table ID
    category = models.ForeignKey('MainCategory', on_delete=models.CASCADE, related_name='pdfs')
    pdf_type = models.CharField(max_length=50, choices=PDF_TYPE_CHOICES)
    pdf_file = models.FileField(upload_to='category_pdfs/')

    def __str__(self):
        return f"{self.category.name} - {self.pdf_type}"

# CategoryImage
class CategoryImage(models.Model):
    imageID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='category_images/')
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"Image {self.imageID} for Category {self.category.name}"

# Manufacturer
class Manufacturer(models.Model):
    manufacturerID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product
class Product(models.Model):
    productID = models.AutoField(primary_key=True)
    Type = models.CharField(max_length=255)
    Kurztext = models.CharField(max_length=255)
    Langtext = models.TextField()
    BestellnummerHersteller = models.CharField(max_length=255)
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.Kurztext

# Product-Manufacturer (junction table)
class ProductManufacturer(models.Model):
    tableID = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_manufacturers')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer_products')

    def __str__(self):
        return f"{self.product.Kurztext} - {self.manufacturer.name}"

# Headings
class Headings(models.Model):
    headingsID = models.AutoField(primary_key=True)
    headingName = models.CharField(max_length=255)

    def __str__(self):
        return self.headingName

# HeadingsDetails
class HeadingsDetails(models.Model):
    generalInfo = models.TextField()
    DetailedInfo = models.TextField()
    heading = models.ForeignKey(Headings, on_delete=models.CASCADE, related_name='details')
    category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='heading_details')

    def __str__(self):
        return f"Details for Heading {self.heading.headingName} in Category {self.category.name}"
