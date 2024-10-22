from rest_framework import serializers 
from myapp.models.userModel import UserModel
 
 
class userDTO(serializers.ModelSerializer):
 
    class Meta:
        model = UserModel
        fields = ('id',
                  'email',
                  'name')
