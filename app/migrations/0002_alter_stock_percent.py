# Generated by Django 4.1.13 on 2025-02-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='percent',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
