from rest_framework import generics
from project.api_user.models import UserTinder
from project.api_user.serializers import UserTinderSerializer
from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny] 
class UserTinderListCreateView(generics.ListCreateAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer

class UserTinderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTinder.objects.all()
    serializer_class = UserTinderSerializer