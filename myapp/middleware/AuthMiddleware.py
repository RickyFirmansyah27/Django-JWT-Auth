import jwt
from myapp.service.authService import AuthService
from django.conf import settings
from functools import wraps
from myapp.response.helper import BaseResponse

def AuthMiddleware(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return BaseResponse('unauthorized', 'Missing or invalid token', None)
        
        try:
            # Get token from header
            token = auth_header.split(' ')[1]
            
            # Decode token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            
            # Verify token type
            if payload.get('token_type') != 'access':
                return BaseResponse('unauthorized', 'Missing or invalid token', None)
            
            # Add user info to request
            request.user_id = payload.get('user_id')
            request.user_email = payload.get('email')
            request.user_role = payload.get('role')
            request.user_full_name = payload.get('full_name')
            
            return view_func(request, *args, **kwargs)
            
        except jwt.ExpiredSignatureError:
            return BaseResponse('unauthorized', 'Token has expired', None)
        except jwt.InvalidTokenError:
            return BaseResponse('unauthorized', 'Invalid token', None)
        except Exception as e:
            return BaseResponse('error', 'Internal server error', None)
    
    return wrapped_view
