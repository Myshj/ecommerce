from rest_framework import routers, serializers, viewsets, urls
from django.contrib.auth.models import User
from serializers import UserSerializer
from products.viewsets import ProductViewSet, CategoryViewSet


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


