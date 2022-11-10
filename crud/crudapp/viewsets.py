from rest_framework import viewsets
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


    filterset_fields= ['name','email']
    search_fields= ['name','email']
    ordering_fields=['name','email']





