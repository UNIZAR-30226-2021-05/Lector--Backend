# Generated by Django 3.1.7 on 2021-04-16 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esAnotacion', models.BooleanField()),
                ('cuerpo', models.CharField(blank=True, max_length=500, null=True)),
                ('offset', models.PositiveBigIntegerField()),
                ('titulo', models.CharField(max_length=20)),
                ('Libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
