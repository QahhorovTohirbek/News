from django.urls import path
from . import views
from dashboard.views import log_in


urlpatterns = [
    path('region/list', views.region_list),
    path('category/list', views.category_list),
    path('post/list', views.post_list),
    path('post/detail/<int:id>/', views.post_detail),
    path('comment/list', views.comment_list),
]
