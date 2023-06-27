# Generated by Django 4.2 on 2023-06-26 06:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateField(default=datetime.datetime.now)),
                ('fecha_devolucion', models.DateField(default=datetime.datetime(2023, 6, 29, 1, 15, 56, 726754))),
                ('ejemplar', models.ManyToManyField(to='app.ejemplar')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name_plural': 'Prestamos',
                'db_table': 'prestamo',
            },
        ),
    ]
