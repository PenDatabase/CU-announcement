# Generated by Django 5.1.4 on 2024-12-24 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('categories', models.CharField(choices=[('Academic', 'Academic'), ('Events', 'Events'), ('Lost_Found', 'Lost & Found'), ('Others', 'Others')], max_length=50)),
                ('description', models.TextField()),
                ('post_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('comment_post_time', models.DateTimeField()),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='announcements.announcements')),
            ],
        ),
    ]
