from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
]
