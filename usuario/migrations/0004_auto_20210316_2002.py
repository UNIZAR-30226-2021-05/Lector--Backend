# Generated by Django 3.1.7 on 2021-03-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20210314_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='tamanoLetra',
            field=models.PositiveIntegerField(default=12),
        ),
    ]
