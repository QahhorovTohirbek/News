from django.urls import path
from . import views
from dashboard.views import log_in


urlpatterns = [
    path('', log_in),
]
