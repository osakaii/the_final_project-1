# Generated by Django 3.2.9 on 2021-11-16 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('color', models.CharField(blank=True, choices=[(1, 'grey'), (2, 'silver'), (3, 'black'), (4, 'red'), (5, 'blue')], max_length=200)),
                ('vin', models.IntegerField(blank=True, default=0)),
                ('brand', models.CharField(blank=True, choices=[(1, 'apple'), (2, 'asus'), (3, 'dell'), (4, 'acer'), (5, 'lenovo')], max_length=200)),
                ('cpu', models.CharField(blank=True, max_length=200)),
                ('ram', models.IntegerField(blank=True, default=0)),
                ('memory', models.IntegerField(blank=True, default=0)),
                ('display', models.CharField(blank=True, choices=[(1, '4096 x 2160'), (2, '2048 x 1080'), (3, '1920 x 1080'), (4, '1024 x 768')], max_length=200)),
                ('battery', models.IntegerField(blank=True, default=0)),
                ('prod', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
