from django.urls import path
from .views import newperrito

urlpatterns = [
    path('adopt/new', newperrito, name="newperrito"),
]