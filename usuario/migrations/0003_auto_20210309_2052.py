# Generated by Django 3.1.7 on 2021-03-09 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_configuracion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
    ]
