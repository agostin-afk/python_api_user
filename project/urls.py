from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project.api_user.views import UserRegistrationView
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
    # path('groups/', include([
    # path('', ProjectGroupView.as_view({'get': 'list', 'post': 'create'}), name='group-list'),  # Listar e criar grupos
    # path('<int:pk>/', ProjectGroupView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='group-detail'),  # Detalhes, atualizar e deletar grupos
    # ])),
    path('api/', include(router.urls)),  # Inclui as URLs geradas pelo router (posts)
]