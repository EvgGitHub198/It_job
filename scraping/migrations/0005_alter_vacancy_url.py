# Generated by Django 4.1.3 on 2022-12-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_alter_vacancy_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='url',
            field=models.URLField(),
        ),
    ]
