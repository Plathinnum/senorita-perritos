from django.urls import path
from .views import home, form,thanks

urlpatterns = [
    path('', home, name="home"),
    path('form/', form, name="form"),
	path('form/thanks/', thanks, name="thanks"),
]