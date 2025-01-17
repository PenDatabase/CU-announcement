# Generated by Django 5.1.4 on 2024-12-30 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comment_post_time',
        ),
        migrations.AddField(
            model_name='announcements',
            name='announcer_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='announcements',
            name='announcer_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('lecturer', 'staff', 'organization')}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
