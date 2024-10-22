from myapp.models.authModel import AuthModel
from django.contrib.auth.hashers import make_password, check_password
from myapp.dto.authDTO import authDTO
from django.contrib.auth.hashers import check_password

from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings

class AuthService:
    ROLE_CHOICES = [
        ('user', 'USER'),
        ('admin', 'ADMIN'),
        ('staff', 'STAFF'),
    ]

    @staticmethod
    def create_user(data):
        existingUser = AuthModel.objects.filter(email=data.get('email')).first()
        if existingUser is not None:
            return None
        
        hashed_password = make_password(data.get('password'))
        
        user = AuthModel(
            email=data.get('email'),
            full_name=data.get('fullName'),
            password=hashed_password,
            role=data.get('role'),
        )
        user.save()
        result = authDTO.toDTO(user)

        return result

    @staticmethod
    def login(data):
        user = AuthModel.objects.filter(email=data.get('username')).first()
            
        if user is None:
            return None
            
        if not check_password(data.get('password'), user.password):
            return False
            
        # Generate JWT tokens
        tokens = AuthService.generate_tokens(user)
            
        # Get user data
        user_data = authDTO.toDTO(user)
        user_data['tokens'] = tokens
            
        return user_data


    @staticmethod
    def generate_tokens(user):
        refresh = RefreshToken.for_user(user)
        
        # Add custom claims to the token
        refresh['email'] = user.email
        refresh['role'] = user.role
        refresh['full_name'] = user.full_name

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'expires_in': int(settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME').total_seconds()),
            'refresh_expires_in': int(settings.SIMPLE_JWT.get('REFRESH_TOKEN_LIFETIME').total_seconds())
        }

    @staticmethod
    def refresh_token(refresh_token):
        refresh = RefreshToken(refresh_token)
        return {
            'access': str(refresh.access_token),
            'expires_in': int(settings.SIMPLE_JWT.get('ACCESS_TOKEN_LIFETIME').total_seconds())
        }

    @staticmethod
    def verify_token(token):
        refresh = RefreshToken(token)
        return refresh