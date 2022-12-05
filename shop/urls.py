from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.list_item, name='list_item'),
    path('shop/<int:id>/', views.detail_item, name='detail_item'),
]