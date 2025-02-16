from django.db import models
from project.api_user.models import UserTinder
from groups.models import ProjectGroup
from django.contrib.auth.models import User

class Post(models.Model):
    group = models.ForeignKey(ProjectGroup, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True, null=True)
    content = models.TextField(blank=True, null=True) #trocar para True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='post_created_by',on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        return f"Post by {self.created_by.name} in {self.group.name}"