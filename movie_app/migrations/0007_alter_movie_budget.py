# Generated by Django 5.0.2 on 2024-03-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_alter_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(blank=True, default=1000000),
        ),
    ]