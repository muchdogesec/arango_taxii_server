# Generated by Django 5.0.6 on 2024-07-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadtask',
            name='password',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
