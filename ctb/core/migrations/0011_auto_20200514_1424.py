# Generated by Django 2.2.12 on 2020-05-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_ctask_c_update_json_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctask',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='status'),
        ),
    ]
