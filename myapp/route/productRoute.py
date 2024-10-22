from django.urls import path
from myapp.controller import productController

urlpatterns = [
    path('api/products', productController.get_products, name='product-list'),
    path('api/products/update', productController.update_product, name='update_product'),
    path('api/products/<int:product_id>', productController.getProductById, name='get_product_by_id'),
]
