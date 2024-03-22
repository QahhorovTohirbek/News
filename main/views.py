from django.shortcuts import render
from . import models

def index(request):
    """ Bosh sahifa """
    region = models.Region.objects.all()
    category = models.Category.objects.all()
    posts = models.Post.objects.all()
    post_img = models.PostImage.objects.all()
    post_vid = models.PostVideo.objects.all()
    comment = models.Comment.objects.all()

    context = {
        'region': region,
        'category': category,
        'posts': posts,
        'post_img': post_img,
        'post_vid': post_vid,
        'comment': comment,
    }
    return render(request, 'front/index.html', context)


def category(request):
    """ Yangiliklar kategoriyasi """
    categories = models.Category.objects.all()
    regions = models.Region.objects.all()
    posts = models.Post.objects.all()

    context = {
        'categories':categories,
        'regions':regions,
        'posts':posts,
    }
    return render(request, 'front/category.html', context)


def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'front/contact.html')

def category_post(request):
    """ Kategoriya va unga tegishli yangiliklar """
    category = models.Category.objects.all()
    post = models.Post.objects.filter(category=category)
    context = {
        'category':category,
        'post':post,
    }

    return render(request, 'front/base.html', context)

def single_news(request, id):
    post = models.Post.objects.get(id=id)
    return render(request, 'front/single_standard.html', {'post':post})