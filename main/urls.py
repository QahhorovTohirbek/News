from django.urls import path
from . import views
from dashboard.views import log_in

app_name = 'main'

urlpatterns = [
    path('', log_in),
    path('region/list', views.region_list),
    path('region/detail/<int:id>/', views.region_detail),
    path('category/list', views.category_list),
    path('category/detail/<int:id>/', views.category_detail),
    path('post/list', views.post_list),
    path('post/detail/<int:id>/', views.post_detail),
]
