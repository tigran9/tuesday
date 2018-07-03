from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(required=True, max_length=255, allow_null=False, allow_blank=False)
    last_name = serializers.CharField(required=True, max_length=255, allow_null=False, allow_blank=False)
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False, max_length=255)
    username = serializers.CharField(max_length=255, required=True, allow_null=False)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['first_name'], validated_data['last_name'],
                                        validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).first() is not None:
            raise ValidationError({'email': "Email already exists"})
        return attrs

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'username',
        ]
