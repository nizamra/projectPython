from django.urls import path     

from .views import home,subjects,about,allTeachers, teacher,teachers,autocomplete,new

from .views import home,subjects,about,allTeachers, suggest, teacher,teachers, teachersBiology, teachersarabic, teachersart, teacherschemistry, teachersenglish, teachershistory, teachersmathematics, teachersmusic, teachersphysics

urlpatterns = [
    path('home', home),
    path('subjects', subjects),
    path('about', about),
    path('allTeachers', allTeachers),
    path('teachers', teachers),
    path('teachers/biology', teachersBiology),
    path('teachers/physics', teachersphysics),
    path('teachers/chemistry', teacherschemistry),
    path('teachers/english', teachersenglish),
    path('teachers/mathematics', teachersmathematics),
    path('teachers/arabic', teachersarabic),
    path('teachers/art', teachersart),
    path('teachers/music', teachersmusic),
    path('teachers/history', teachershistory),
    path('suggest', suggest),
    path('teacher/<int:teacherId>', teacher),
    path('search/<str>', autocomplete),
    path('new', new)
]


