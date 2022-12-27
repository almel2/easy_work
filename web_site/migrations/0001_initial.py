# Generated by Django 4.1.4 on 2022-12-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=511, verbose_name='Title')),
                ('url', models.URLField(max_length=511, verbose_name='URL')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('date', models.CharField(max_length=255, verbose_name='Date')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
            ],
        ),
    ]
