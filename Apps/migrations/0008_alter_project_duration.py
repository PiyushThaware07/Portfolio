# Generated by Django 4.1.6 on 2023-07-02 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0007_project_technologyused'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.IntegerField(),
        ),
    ]