from django.conf.urls import url
from .views import upload_file, obtenerOficinas, obtenerCarpetas
urlpatterns = [
  url(r'^upload/$', upload_file, name='file-upload'),
  url(r'^oficinas/$', obtenerOficinas, name='oficinas'),
  url(r'^carpetas/$', obtenerCarpetas, name='folders'),
]