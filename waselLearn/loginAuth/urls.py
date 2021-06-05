from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('', success, name = 'success'),
	path('form', imageView, name = 'image_upload'),
	path('teachers', teachers),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)



# urlpatterns = [
#     path('loginAuth', views.index),
#     path('form', views.form),
#     path('showAll', views.showAll),
#     path('register', views.register),
# ]