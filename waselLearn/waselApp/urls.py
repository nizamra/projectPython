from django.urls import path     
from . import views
urlpatterns = [
    path('subjects', views.subjects),
    path('about', views.about),
    path('allTeachers', views.allTeachers),
    path('teachers', views.teachers),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
]


