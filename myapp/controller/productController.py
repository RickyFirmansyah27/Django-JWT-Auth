import logging
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from myapp.models.productModel import ProductModel
from myapp.dto.productDTO import productDTO
from myapp.response.helper import BaseResponse
from myapp.middleware.AuthMiddleware import AuthMiddleware 
from django.views.decorators.http import require_http_methods
# Configure logging
logger = logging.getLogger(__name__)

@require_http_methods(['GET', 'PUT', 'DELETE'])
@AuthMiddleware
def getProducts(request):
    if request.method == 'GET':
        products = ProductModel.objects.all()
        response = productDTO(products, many=True)
        logger.info('[ProductController] - Fetched all products successfully.', extra={'data': response.data})
        return BaseResponse('success', 'Successfully fetched products', response.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        product = get_object_or_404(ProductModel, id=data.get('id'))

        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.save()

        response = productDTO(product)
        return BaseResponse('success', 'Successfully updated product', response.data)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        product = get_object_or_404(ProductModel, id=data.get('id'))

        product.delete()
        return BaseResponse('success', 'Successfully deleted product', None)

@require_http_methods(['GET'])
@AuthMiddleware
def getProductById(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    response = productDTO(product)
    logger.info('[ProductController] - Successfully fetched product by ID', extra={'data': response.data})
    return BaseResponse('success', 'Successfully fetched product', response.data)
