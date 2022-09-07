# Generated by Django 4.1 on 2022-08-21 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=200)),
                ('project_description', models.TextField(null=True)),
                ('complete', models.BooleanField(default=True)),
                ('project_image', models.ImageField(upload_to='images')),
                ('agix_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('employee_major', models.CharField(max_length=50)),
                ('employee_description', models.TextField(null=True)),
                ('employee_profile_picture', models.ImageField(upload_to='images')),
                ('employee_previous_project', models.ManyToManyField(to='Staff_Projects.projects')),
            ],
        ),
    ]