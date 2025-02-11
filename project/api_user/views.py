from rest_framework import generics
from rest_framework import viewsets
from project.api_user.models import UserTinder, ProjectGroup
from project.api_user.serializers import UserTinderSerializer
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer, ProjectGroupSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny] 
class UserTinderListCreateView(generics.ListCreateAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer

class UserTinderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer
    
class ProjectGroupView(viewsets.ModelViewSet):
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam criar grupos

    def perform_create(self, serializer):
        # Define o `created_by` como o usuário logado
        serializer.save(created_by=self.request.user)