# Generated by Django 4.1.6 on 2023-02-27 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools_and_tasks', '0015_alter_taskcomment_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(auto_created=True, blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
