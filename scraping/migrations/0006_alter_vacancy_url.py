# Generated by Django 4.1.3 on 2022-12-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_alter_vacancy_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
