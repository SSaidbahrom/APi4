from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status,permissions
from datetime import datetime 
from .models import Category, Product
from .serializers import ParentCategoryModelSerializer,ProductSerializer,CreateCategorySerializer,CreateProductSerializer,ProductListSerializer
from .permissions import ISCayomBlocked,WorkDay
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class ParentCategoryListApiView(ListAPIView):
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        return Category.objects.filter(parent__isnull=True)


class ChildrenCategoryByCategorySlug(ListAPIView):
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        parent = Category.objects.filter(slug=category_slug).first()
        if not parent:
            return Category.objects.none()
        return parent.children.all()
 

class ProductListByChildCategorySlug(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [WorkDay]

    def get_queryset(self):
        parent_slug = self.kwargs['slug']
        child_slug = self.kwargs['child_slug']

        parent_category = Category.objects.filter(slug=parent_slug).first()
        if not parent_category:
            return Product.objects.none()

        child_category = parent_category.children.filter(slug=child_slug).first()
        if not child_category:
            return Product.objects.none()

        return child_category.products.all()


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'token': token.key
        })
    
class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ProductListAPiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer



