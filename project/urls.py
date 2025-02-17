from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from project.api_user.views import UserRegistrationView, user_login, user_logout
from groups.views import ProjectGroupView
from posts.views import PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', ProjectGroupView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/', include(router.urls)),
]
