from rest_framework import serializers
from .models import Category, Product, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    image_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'image_count', 'images']

    def get_image_count(self, obj):
        return obj.images.count()

class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','description','price','category')

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','images']

class ParentCategoryModelSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'

    def get_product_count(self, obj):
        count = obj.products.count()
        for child in obj.children.filter(is_active=True):
            count += self.get_product_count(child)
        return count
