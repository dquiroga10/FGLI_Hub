from . import views
from django.urls import path


urlpatterns = [
    path('', views.network, name='network'),
]