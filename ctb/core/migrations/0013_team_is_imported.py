# Generated by Django 2.2.12 on 2020-05-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200516_0259_squashed_0023_auto_20200516_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_imported',
            field=models.BooleanField(default=False, verbose_name='is imported?'),
        ),
    ]
