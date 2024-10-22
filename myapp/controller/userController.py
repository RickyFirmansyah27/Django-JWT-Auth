import logging
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from myapp.models.userModel import UserModel
from myapp.dto.userDTO import userDTO
from myapp.response.helper import BaseResponse
from myapp.middleware.AuthMiddleware import AuthMiddleware 
from django.views.decorators.http import require_http_methods

# Configure logging
logger = logging.getLogger(__name__)

@require_http_methods(['GET', 'PUT'])
@AuthMiddleware
def getUsers(request):
    if request.method == 'GET':
        users = UserModel.objects.all()
        response = userDTO(users, many=True)
        logger.info('[UserController] - Fetched all user successfully.', extra={'data': response.data})
        return BaseResponse('success', 'Successfully fetched users', response.data)
     
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        user = get_object_or_404(UserModel, id=data.get('id')) 

        user.email = data.get('email', user.email)
        user.name = data.get('name', user.name)   
        user.save()

        response = userDTO(user)

        return BaseResponse('success', 'Successfully updated user', response.data)

    elif request.method == 'DELETE':
            data = JSONParser().parse(request)
            user = get_object_or_404(UserModel, id=data.get('id'))

            user.delete()

            return BaseResponse('success', 'Successfully deleted user', None)