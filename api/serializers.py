from rest_framework.serializers import ModelSerializer, Serializer
from main import models


class RegionSerializerList(ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['name']



class CategorySerializerList(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']



class PostSerializerList(ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id','title']


class PostSerializerDetail(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class CommentSerializerCreate(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class CommentSerializerList(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['text']
        


class ContactSerializerCreate(ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'
        