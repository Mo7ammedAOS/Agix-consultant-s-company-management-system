# Generated by Django 4.1 on 2022-08-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff_Projects', '0002_alter_projects_project_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='employee_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
