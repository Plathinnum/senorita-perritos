from django.contrib import admin
from django.urls import path, include
from .views import form,thanks

urlpatterns = [
    path('form/', form, name="form"),
	path('form/thanks/', thanks, name="thanks"),
    path('admin/',admin.site.urls),
]