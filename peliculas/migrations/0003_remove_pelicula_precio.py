# Generated by Django 5.0.6 on 2024-05-24 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_pelicula_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='precio',
        ),
    ]
