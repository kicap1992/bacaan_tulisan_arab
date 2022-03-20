from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('bacaans/', views.getBacaans),
    path('bacaans/<str:pk>/', views.getBacaan),
]
