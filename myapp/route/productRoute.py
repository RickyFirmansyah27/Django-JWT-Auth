from django.urls import path
from myapp.controller import productController

urlpatterns = [
    path('api/products', productController.getProducts, name='product-list'),
    path('api/products/<int:product_id>/', productController.getProductById, name='get_product_by_id'),
]
