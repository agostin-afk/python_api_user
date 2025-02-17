from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project.api_user.views import UserRegistrationView, user_login, user_logout
from groups.views import ProjectGroupView
from posts.views import PostViewSet

# Configuração do router para o PostViewSet
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)  # Registra as URLs para o PostViewSet
router.register(r'groups', ProjectGroupView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # URLs de autenticação do DRF
    path('register/', UserRegistrationView.as_view(), name='register'),  # Rota de registro de usuário
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/', include(router.urls)),  # Inclui as URLs geradas pelo router (posts)
]