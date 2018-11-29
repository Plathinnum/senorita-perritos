from django.urls import path, include
from .views import signup
from django.contrib import admin

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]