from django.urls import path     
from . import views
urlpatterns = [
    path('loginAuth', views.index),
]