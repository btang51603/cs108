# Generated by Django 4.0.3 on 2022-04-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_deck_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='date_rented',
            field=models.DateTimeField(blank=True),
        ),
    ]
