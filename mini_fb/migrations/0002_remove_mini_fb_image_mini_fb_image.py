# Generated by Django 4.0.3 on 2022-03-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mini_fb',
            name='image',
        ),
        migrations.AddField(
            model_name='mini_fb',
            name='Image',
            field=models.URLField(blank=True),
        ),
    ]
