# Generated by Django 4.2.2 on 2023-10-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_crud_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='time',
            field=models.TimeField(default=False),
        ),
    ]
