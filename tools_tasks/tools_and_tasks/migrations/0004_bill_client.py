# Generated by Django 4.1.6 on 2023-02-10 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools_and_tasks', '0003_remove_constructionobject_bill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.client'),
        ),
    ]