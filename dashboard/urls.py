from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),

    #Kategoriya
    path('create-category', views.create_category, name='create_category'),
    path('list-category', views.list_category, name='list_category'),
    path('update-category/<int:id>/', views.update_category, name='update_category'),
    path('delete-category/<int:id>/', views.delete_category, name='delete_category'),
    path('detail-category/<int:id>/', views.detail_category, name='detail_category'),

    #Post
    path('create-post', views.create_post, name='create_post'),
    path('list-post', views.list_post, name='list_post'),
    path('update-post/<int:id>/', views.update_post, name='update_post'),
    path('delete-post/<int:id>/', views.delete_post, name='delete_post'),

    # Avtorizatsiya
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    
]