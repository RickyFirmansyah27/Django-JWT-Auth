from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from myapp.response.helper import BaseResponse
from rest_framework.parsers import JSONParser
from myapp.service.authService import AuthService

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        data = JSONParser().parse(request)
        auth_service = AuthService()
        response = auth_service.create_user(data)
        if(response is None):
            logger.info(f'[AuthController] - User already exists')
            return BaseResponse('error', 'User already exists', None)

        logger.info('[AuthController] - Successfully created user', extra={'data': response})
        return BaseResponse('success', 'Successfully created user', response)

    except Exception as err:
        logger.error(f'[AuthController] - {err}')
        return BaseResponse(None, 'Internal server error', None)


@api_view(['POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        auth_service = AuthService()
        response = auth_service.login(data)
        if(response is None or False):
            return BaseResponse('error', 'Unauthorized', None)

        print('RESULT', response)
        logger.info('[AuthController] - Successfully login user', extra={'data': response})
        return BaseResponse('success', 'Successfully login user', response)

    except Exception as err:
        logger.error('[AuthController] - {err}')
        return BaseResponse(None, 'Internal server error', None)