from django.urls import path     
from .views import home,subjects,about,allTeachers,teachers
urlpatterns = [
    path('home', home),
    path('subjects', subjects),
    path('about', about),
    path('allTeachers', allTeachers),
    path('teachers', teachers),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
]


