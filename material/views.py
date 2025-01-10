from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MainCategory, CategoryImage, Manufacturer, Product, ProductManufacturer, Headings, HeadingsDetails, CategoryPDF
from .serializers import (
    MainCategorySerializer,
    CategoryImageSerializer,
    ManufacturerSerializer,
    ProductSerializer,
    ProductManufacturerSerializer,
    HeadingsSerializer,
    HeadingsDetailsSerializer,
    CategoryPDFSerializer
)

# View for MainCategory
class MainCategoryListView(APIView):
    def get(self, request):
        categories = MainCategory.objects.all()
        serializer = MainCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryPDFFilterView(APIView):
    """
    View to get PDFs filtered by categoryID.
    """

    def get(self, request):
        # Get the categoryID from query parameters
        categoryID = request.query_params.get('categoryID')

        if categoryID:
            # Validate if the category exists
            try:
                categoryID = int(categoryID)  # Convert to integer for validation
                pdfs = CategoryPDF.objects.filter(category=categoryID)
                if not pdfs.exists():
                    return Response(f"No images found for categoryID {categoryID}")
            except ValueError:
                return Response({"error": "Invalid categoryID format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If no categoryID, return error 
            return Response({"error": "Invalid categoryID format"}, status=status.HTTP_400_BAD_REQUEST)


        # Serialize the products
        serializer = CategoryPDFSerializer(pdfs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for CategoryImage
class CategoryImageListView(APIView):
    def get(self, request):
        # Get the categoryID from query parameters
        categoryID = request.query_params.get('categoryID')

        if categoryID:
            # Validate if the category exists
            try:
                categoryID = int(categoryID)  # Convert to integer for validation
                images = CategoryImage.objects.filter(category=categoryID)
                if not images.exists():
                    return Response(f"No images found for categoryID {categoryID}")
            except ValueError:
                return Response({"error": "Invalid categoryID format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If no categoryID, return error 
            return Response({"error": "Invalid categoryID format"}, status=status.HTTP_400_BAD_REQUEST)


        # Serialize the products
        serializer = CategoryImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for Manufacturer
class ManufacturerListView(APIView):
    def get(self, request):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for Product
class ProductListView(APIView):
    def get(self, request):
        # Get the categoryID from query parameters
        categoryID = request.query_params.get('categoryID')

        if categoryID:
            # Validate if the category exists
            try:
                categoryID = int(categoryID)  # Convert to integer for validation
                products = Product.objects.filter(category_id=categoryID)
                if not products.exists():
                    return Response(f"No products found for categoryID {categoryID}")
            except ValueError:
                return Response({"error": "Invalid categoryID format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # If no categoryID, return all products
            products = Product.objects.all()

        # Serialize the products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# View for ProductManufacturer (junction table)
class ProductManufacturerListView(APIView):
    def get(self, request):
        product_manufacturers = ProductManufacturer.objects.all()
        serializer = ProductManufacturerSerializer(product_manufacturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# View for Headings
class HeadingsListView(APIView):
    def get(self, request):
        headings = Headings.objects.all()
        serializer = HeadingsSerializer(headings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HeadingsDetailsListView(APIView):
    """
    Fetch heading details filtered by MainCategory ID.
    """

    def get(self, request, *args, **kwargs):
        try:
            main_category_id = request.query_params.get('categoryID')
            print(main_category_id)
            # Validate if MainCategory exists
            main_category = MainCategory.objects.filter(categoryID=main_category_id).first()
            if not main_category:
                return Response(
                    {"error": "MainCategory with the given ID does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            
            # Filter HeadingDetails by the given MainCategory
            heading_details = HeadingsDetails.objects.filter(category=main_category)
            serializer = HeadingsDetailsSerializer(heading_details, many=True)
 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )