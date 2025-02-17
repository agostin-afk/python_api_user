from rest_framework import generics
from rest_framework import viewsets
from project.api_user.models import UserTinder
from .models import ProjectGroup
from project.api_user.serializers import UserTinderSerializer
from rest_framework import generics, permissions
from .serializers import ProjectGroupSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectGroupView(viewsets.ModelViewSet):
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam criar grupos

    def perform_create(self, serializer):
        # Define o `created_by` como o usuário logado
        serializer.save(created_by=self.request.user)
