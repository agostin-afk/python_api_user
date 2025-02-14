# Generated by Django 5.1.5 on 2025-02-13 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0003_projectgroup_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='projectgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='project_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
