from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ProjectGroup

class ProjectGroupSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        required=False,  # Torna o campo opcional durante a atualização
        allow_null=True  # Permite que o campo seja nulo
    )
    member_emails = serializers.ListField(
        child=serializers.EmailField(),
        write_only=True,  # Campo apenas para escrita (não aparece na resposta)
        required=False
    )

    class Meta:
        model = ProjectGroup
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'created_by', 'members', 'member_emails']
        read_only_fields = ['members']  # O campo members é apenas leitura

    def create(self, validated_data):
        # Extrai os emails dos membros
        member_emails = validated_data.pop('member_emails', [])
        
        # Cria o ProjectGroup
        project_group = ProjectGroup.objects.create(**validated_data)
        
        # Adiciona os membros ao grupo
        for email in member_emails:
            try:
                user = User.objects.get(email=email)
                project_group.members.add(user)
            except User.DoesNotExist:
                pass  # Ignora emails que não correspondem a usuários
        
        return project_group

    def update(self, instance, validated_data):
        # Extrai os emails dos membros
        member_emails = validated_data.pop('member_emails', None)
        
        # Atualiza os campos do ProjectGroup
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        
        # Atualiza os membros, se fornecido
        if member_emails is not None:
            instance.members.clear()  # Remove todos os membros existentes
            for email in member_emails:
                try:
                    user = User.objects.get(email=email)
                    instance.members.add(user)
                except User.DoesNotExist:
                    pass  # Ignora emails que não correspondem a usuários
        
        instance.save()
        return instance