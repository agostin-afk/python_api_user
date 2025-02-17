from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework import viewsets
from project.api_user.models import UserTinder
from project.api_user.serializers import UserTinderSerializer
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from groups.models import ProjectGroup
from groups.serializers import ProjectGroupSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny] 
class UserTinderListCreateView(generics.ListCreateAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer

class UserTinderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer
    
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import UserTinder  # Certifique-se de importar o modelo UserTinder corretamente

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        if '@' in username:
            try:
                user = UserTinder.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)  # Agora isso deve funcionar
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    # Obtém o token do usuário, se existir
    token = getattr(request.user, 'auth_token', None)
    
    if token:
        token.delete()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    
    return Response({'error': 'User is not logged in or token does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
# class ProjectGroupView(viewsets.ModelViewSet):
#     queryset = ProjectGroup.objects.all()
#     serializer_class = ProjectGroupSerializer
#     permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados possam criar grupos

#     def perform_create(self, serializer):
#         # Define o `created_by` como o usuário logado
#         serializer.save(created_by=self.request.user)