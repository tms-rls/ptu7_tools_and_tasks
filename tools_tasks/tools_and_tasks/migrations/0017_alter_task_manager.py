# Generated by Django 4.1.6 on 2023-02-27 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools_and_tasks', '0016_task_manager_alter_task_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
