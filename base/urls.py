from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bacaan/<str:pk>', views.bacaan, name='bacaan'),
]
