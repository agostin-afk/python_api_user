from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectGroupView

router = DefaultRouter()
router.register(r'groups/register', ProjectGroupView.as_view({'get': 'list', 'post': 'create'}))
router.register(r'groups/<int:pk>/', ProjectGroupView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}))


urlpatterns = [
    path('', include(router.urls)),
]