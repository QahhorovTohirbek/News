from django.shortcuts import render
from django.contrib.auth.models import User
from main import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(['GET'])
def region_list(request):
    region = models.Region.objects.all()
    region_serializer = serializers.RegionSerializerList(region, many=True)

    return Response(region_serializer.data)



@api_view(['GET'])
def category_list(request):
    category = models.Category.objects.all()
    category_serializer = serializers.CategorySerializerList(category, many=True)

    return Response(category_serializer.data)


@api_view(['GET'])
def post_list(request):
    post = models.Post.objects.all()
    post_serializer = serializers.PostSerializerList(post, many=True)


    return Response(post_serializer.data)


@api_view(['GET'])
def post_detail(request, id):
    post = models.Post.objects.get(id=id)
    post_serializer = serializers.PostSerializerDetail(post)

    return Response(post_serializer.data)


@api_view(['GET', 'POST'])
def comment_create(request):
    if request.method == 'POST':
        comment_serializer = serializers.CommentSerializerCreate(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data, status=201)
        
        return Response(comment_serializer.errors, status=400)


@api_view(['GET'])
def comment_list(request):
    comment = models.Comment.objects.all()
    comment_serializer = serializers.CommentSerializerList(comment, many=True)

    return Response(comment_serializer.data)



@api_view(['POST'])
def contact_create(request):
    if request.method == 'POST':
        contact_serializer = serializers.ContactSerializerCreate(data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data, status=201)
        
        return Response(contact_serializer.errors, status=400)
    