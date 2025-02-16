from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'group', 'content', 'created_at', 'updated_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Define o autor como o usuário logado
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)