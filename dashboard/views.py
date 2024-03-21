from django.shortcuts import render, redirect
from main import models
from django.contrib.auth.models import User


def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()
    users = User.objects.count()
    context = {
        'contacts':contacts,
        'users':users,
    }
    return render(request, 'dashboard/index.html', context)