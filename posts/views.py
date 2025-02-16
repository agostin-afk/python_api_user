from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  # Apenas usuários autenticados podem criar posts

    def get_queryset(self):
        # Filtra os posts pelo grupo, se um group_id for fornecido na query string
        group_id = self.request.query_params.get('group_id')
        if group_id:
            return Post.objects.filter(group_id=group_id)
        return Post.objects.all()

    def perform_create(self, serializer):
        # Define o autor como o usuário logado
        serializer.save(created_by=self.request.user)