# Generated by Django 4.1.6 on 2023-07-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0009_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='fullName',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
