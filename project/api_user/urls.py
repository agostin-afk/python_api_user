from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, ProjectGroupView

router = DefaultRouter()
router.register(r'register', UserRegistrationView.as_view(), name='register')

    path('', include(router.urls)),
]