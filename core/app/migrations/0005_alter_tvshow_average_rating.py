# Generated by Django 5.0.6 on 2024-05-30 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_tvshow_runtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tvshow',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
    ]
