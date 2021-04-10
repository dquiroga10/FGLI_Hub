from . import views
from django.urls import path


urlpatterns = [
    path('', views.network, name='home'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('mentorapp/', views.mentorapp, name='mentorapp'),
    path('newquestion/', views.create_question, name='questions'),
]