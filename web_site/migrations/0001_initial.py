# Generated by Django 4.1.4 on 2023-01-30 15:25

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
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='SiteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255, verbose_name='Name_site')),
            ],
        ),
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=511, verbose_name='Title')),
                ('url', models.URLField(max_length=511, verbose_name='URL')),
                ('date', models.CharField(max_length=255, verbose_name='Date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.citymodel')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.sitemodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
