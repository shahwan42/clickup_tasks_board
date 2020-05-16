# Generated by Django 2.2.12 on 2020-05-16 04:03

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('core', '0012_auto_20200516_0259'), ('core', '0013_auto_20200516_0307'), ('core', '0014_auto_20200516_0309'), ('core', '0015_auto_20200516_0311'), ('core', '0016_auto_20200516_0312'), ('core', '0017_auto_20200516_0312'), ('core', '0018_auto_20200516_0313'), ('core', '0019_auto_20200516_0313'), ('core', '0020_auto_20200516_0313'), ('core', '0021_auto_20200516_0316'), ('core', '0022_auto_20200516_0317'), ('core', '0023_auto_20200516_0348')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20200514_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ctask',
            name='c_json_res',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, verbose_name='TaskCreated JSON Response'),
        ),
        migrations.AlterField(
            model_name='ctask',
            name='c_list',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.CList'),
        ),
        migrations.AlterField(
            model_name='ctask',
            name='user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RenameField(
            model_name='cfolder',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.RenameField(
            model_name='clist',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.RenameField(
            model_name='cspace',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.RenameField(
            model_name='cspace',
            old_name='c_team',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='ctask',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.AlterField(
            model_name='ctask',
            name='clickup_id',
            field=models.CharField(editable=False, max_length=12, unique=True, verbose_name='ClickUp ID'),
        ),
        migrations.RenameField(
            model_name='cteam',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.RenameField(
            model_name='webhook',
            old_name='c_id',
            new_name='clickup_id',
        ),
        migrations.RenameField(
            model_name='webhook',
            old_name='c_team',
            new_name='team',
        ),
        migrations.RenameModel(
            old_name='CTeam',
            new_name='Team',
        ),
        migrations.RenameModel(
            old_name='CSpace',
            new_name='Space',
        ),
        migrations.RenameModel(
            old_name='CFolder',
            new_name='Folder',
        ),
        migrations.RenameModel(
            old_name='CTask',
            new_name='Task',
        ),
        migrations.RenameField(
            model_name='folder',
            old_name='c_space',
            new_name='space',
        ),
        migrations.RenameModel(
            old_name='CList',
            new_name='List',
        ),
        migrations.RenameField(
            model_name='list',
            old_name='c_folder',
            new_name='folder',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='c_list',
            new_name='_list',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='c_json_res',
            new_name='created_json',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='c_update_json_res',
            new_name='updated_json',
        ),
        migrations.RenameField(
            model_name='webhook',
            old_name='c_json_res',
            new_name='created_json',
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={},
        ),
        migrations.AlterModelOptions(
            name='space',
            options={},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.AlterField(
            model_name='task',
            name='_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.List'),
        ),
        migrations.AlterField(
            model_name='task',
            name='clickup_id',
            field=models.CharField(max_length=12, unique=True, verbose_name='ClickUp ID'),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
