from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Add this import
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('authentication/', include('login_system.urls')),
    # Add this logout URL pattern
    path('authentication/logout/', auth_views.LogoutView.as_view(), name='logout'),
]