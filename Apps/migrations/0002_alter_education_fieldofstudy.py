# Generated by Django 4.1.6 on 2023-07-01 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='fieldofstudy',
            field=models.CharField(max_length=256, null=True),
        ),
    ]