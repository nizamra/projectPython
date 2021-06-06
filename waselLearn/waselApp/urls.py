from django.urls import path     
from .views import home,subjects,about,allTeachers, teacher,teachers
urlpatterns = [
    path('home', home),
    path('subjects', subjects),
    path('about', about),
    path('allTeachers', allTeachers),
    path('teachers', teachers),
    path('teacher/<int:teacherId>', teacher),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
]


