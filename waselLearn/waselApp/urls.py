from django.urls import path     
from . import views
urlpatterns = [
    path('/subjects', views.subjects),
    path('/about', views.about),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
]


