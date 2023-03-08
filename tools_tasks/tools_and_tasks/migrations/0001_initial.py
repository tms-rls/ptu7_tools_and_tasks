# Generated by Django 4.1.6 on 2023-02-10 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('number', models.CharField(help_text='Insert number of bill', max_length=10, verbose_name='Number of bill')),
                ('status', models.CharField(choices=[('p', 'Paid'), ('u', 'Unpaid'), ('c', 'Canceled')], default='u', help_text='Status of the bill', max_length=1, verbose_name='Status')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Payment by date')),
                ('amount', models.FloatField(help_text='Insert amount of the bill', verbose_name='Amount')),
            ],
            options={
                'ordering': ['payment_date'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Insert client's name", max_length=100, verbose_name='Name')),
                ('contact_phone', models.CharField(blank=True, help_text="Insert client's contact phone number", max_length=50, null=True, verbose_name='Contact phone')),
                ('contact_address', models.CharField(blank=True, help_text="Insert client's contact address", max_length=50, null=True, verbose_name='Contact address')),
                ('contact_email', models.CharField(blank=True, help_text="Insert client's contact email", max_length=100, null=True, verbose_name='Contact email')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Insert address of construction object', max_length=200, verbose_name='Address')),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.bill')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.client')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Insert employee's name", max_length=100, verbose_name='Name')),
                ('surname', models.CharField(help_text="Insert employee's surname", max_length=100, verbose_name='Surname')),
                ('position', models.CharField(blank=True, help_text="Insert employee's position", max_length=100, null=True, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insert tool', max_length=100, verbose_name='Tool')),
                ('inventory_number', models.CharField(help_text='Insert inventory number', max_length=100, verbose_name='Inventory number')),
                ('status', models.CharField(choices=[('a', 'Available'), ('b', 'Broken'), ('r', 'In repair'), ('t', 'Taken')], default='a', help_text='Status of the tool', max_length=1, verbose_name='Status')),
                ('construction_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.constructionobject')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('name', models.CharField(help_text='Insert task', max_length=100, verbose_name='Task')),
                ('notes', models.TextField(blank=True, help_text="Insert task's notes", max_length=2000, null=True, verbose_name='Notes')),
                ('deadline', models.DateTimeField(blank=True, null=True, verbose_name='Accomplish till')),
                ('status', models.CharField(choices=[('a', 'Assigned'), ('p', 'In progress'), ('f', 'Finished'), ('c', 'Canceled')], default='a', help_text='Status of the task', max_length=1, verbose_name='Status')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.employee')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='constructionobject',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools_and_tasks.employee'),
        ),
    ]
