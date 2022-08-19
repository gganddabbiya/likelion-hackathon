from django.urls import path
from . import views

urlpatterns = [
    path('postcreate/', views.postcreate, name='postcreate'),
    path('freeposts/', views.freeposts, name='freeposts_list'),
    path('freedetail/<int:pk>', views.freePostDetail, name='freeposts_detail'),
]