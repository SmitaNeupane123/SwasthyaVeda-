from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from typing import Any, Dict

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    first_name:str = serializers.CharField(required=True)
    last_name :str= serializers.CharField(required=True)

    class Meta:
        model = User
        fields:list[str] = ['username', 'email', 'password', 'role', 'first_name', 'last_name']
        extra_kwargs:Dict = {'password': {'write_only': True}}

    def create(self, validated_data: Dict[str, Any]) -> str:
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data.get('role', 'doctor')
        )
        return user

class LoginSerializer(serializers.Serializer):
    username:str = serializers.CharField()
    password:str = serializers.CharField()

    def validate(self, data: Dict[str, str]) -> Dict[str, Any]:
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise AuthenticationFailed("Invalid credentials")
        return {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': user.role
        }
# obj form lai json format ma change gareko ... yo duita ko kam nai tei ho ... register ra login ko lagi jwt use gareko cham 