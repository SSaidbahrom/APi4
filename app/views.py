from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime 
from .models import Category, Product
from .serializers import ParentCategoryModelSerializer,ProductSerializer,CreateCategorySerializer,CreateProductSerializer,ProductListSerializer
from rest_framework import permissions
from .permissions import ISCayomBlocked,WorkDay

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


class ProductCreateApiView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductListAPiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
