from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime 
from .models import Category, Product
from .serializers import ParentCategoryModelSerializer,ProductSerializer,CreateCategorySerializer,CreateProductSerializer,ProductListSerializer


class ParentCategoryListApiView(ListAPIView):
    queryset  =Category.objects.all()
    serializer_class = ParentCategoryModelSerializer


    def get_queryset(self):
        queryset = Category.objects.filter(parent__isnull = True)
        return queryset


class ChildrenCategoryByCategorySlug(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoryModelSerializer

    def get_queryset(self):
        category_slug = self.kwargs['slug']
        queryset = Category.objects.filter(slug=category_slug).first()
        if not queryset:
            return Category.objects.none()
        
        return queryset.children.all()

class ProductListByChildCategorySlug(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.filter(slug=slug).first()
        if not category:
            return Product.objects.none()
        return Product.objects.filter(category=category)


class CategoryCreateApiView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer

class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class ProductListAPiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer