from django.urls import path
from rest_framework import views

from .import views
from .views import BlogView

app_name = 'blog'

urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('', views.blogList, name="events"),
    path('detail/<str:slug>/', views.blogDetail, name="detail"),
    path('create', views.blogCreate, name="create"),
    path('update/<str:slug>/', views.blogUpdate, name="update"),
    path('delete/<str:slug>/', views.blogDelete, name="delete"),
 ]