from django.urls import path
from .views import (
    MainCategoryListView,
    CategoryImageListView,
    ManufacturerListView,
    ProductListView,
    ProductManufacturerListView,
    HeadingsListView,
    HeadingsDetailsListView,
    CategoryPDFFilterView
)

urlpatterns = [
    path('categories/', MainCategoryListView.as_view(), name='main-category-list'),
    path('category-images/', CategoryImageListView.as_view(), name='category-image-list'),
    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('product-manufacturers/', ProductManufacturerListView.as_view(), name='product-manufacturer-list'),
    path('headings/', HeadingsListView.as_view(), name='headings-list'),
    path('heading-details/', HeadingsDetailsListView.as_view(), name='headings-details-list'),
    path('category-pdfs/', CategoryPDFFilterView.as_view(), name='category-pdfs-list'),
]
