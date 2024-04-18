from django.shortcuts import render
from django.contrib.auth.models import User
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required




@login_required(login_url='dashboard:log_in')
@api_view(['GET'])
def region_list(request):
    region = models.Region.objects.all()
    region_serializer = serializers.RegionSerializerList(region, many=True)

    return Response(region_serializer.data)


@login_required(login_url='dashboard:log_in')
@api_view(['GET'])
def region_detail(request, id):
    region = models.Region.objects.get(id=id)
    region_serializer = serializers.RegionSerializerDetail(region)

    return Response(region_serializer.data)


@login_required(login_url='dashboard:log_in')
@api_view(['GET'])
def category_list(request):
    category = models.Category.objects.all()
    category_serializer = serializers.CategorySerializerList(category, many=True)

    return Response(category_serializer.data)


@login_required(login_url='dashboard:log_in')
@api_view(['GET'])
def category_detail(request, id):
    category = models.Category.objects.get(id=id)
    category_serializer = serializers.CategorySerializerDetail(category)

    return Response(category_serializer.data)


@login_required(login_url='dashboard:log_in')
@api_view(['GET'])
def post_list(request):
    post = models.Post.objects.all()
    post_serializer = serializers.PostSerializerList(post, many=True)


    return Response(post_serializer.data)


@login_required(login_url='dashboard:log_in')
@api_view(['GET', 'POST'])
def post_detail(request, id):
    post = models.Post.objects.get(id=id)
    post_serializer = serializers.PostSerializerDetail(post)

    return Response(post_serializer.data)