# Generated by Django 4.2.2 on 2023-11-19 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_remove_profile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.profile'),
        ),
    ]