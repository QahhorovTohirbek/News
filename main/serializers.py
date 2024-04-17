from rest_framework.serializers import ModelSerializer, Serializer
from main import models


class RegionSerializerList(ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['name']


class RegionSerializerDetail(ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'



class CategorySerializerList(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']



class CategorySerializerDetail(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'



class PostSerializerList(ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title']


class PostSerializerDetail(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
        depth=1
        