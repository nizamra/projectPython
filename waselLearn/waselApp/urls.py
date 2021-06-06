from django.urls import path     
from .views import home,subjects,about,allTeachers, suggest, teacher,teachers
urlpatterns = [
    path('home', home),
    path('subjects', subjects),
    path('about', about),
    path('allTeachers', allTeachers),
    path('teachers', teachers),
    path('suggest', suggest),
    path('teacher/<int:teacherId>', teacher),
    # path('waselApp/', views.),
    # path('waselApp/', views.),
]


