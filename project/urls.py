from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project.api_user.views import UserRegistrationView # Certifique-se de que o caminho está correto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', UserRegistrationView.as_view(), name='register'),  # Rota de registro
]