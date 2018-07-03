from django.contrib.auth.models import User
from rest_framework import serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch', 'put')
    permission_classes = ()
