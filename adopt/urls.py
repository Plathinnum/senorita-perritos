from .views import galeria, adoptados, home, listar
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('galeria/', galeria, name="galeria"),
    url('adopcion/', adoptados, name="adopcion"),
    url(r'^$', views.home,name='home'),
    url(r'^perrito/(?P<id>[0-9]+)/editar/$', views.editar,name='editarperrito'),
    url('listar/', listar, name="listar")
]

