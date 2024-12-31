# Generated by Django 5.1.4 on 2024-12-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0006_alter_announcement_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='category',
            field=models.CharField(choices=[('Official', 'Official'), ('Academic', 'Academic'), ('Events', 'Events'), ('Lost_Found', 'Lost & Found'), ('Others', 'Others')], max_length=50),
        ),
    ]
