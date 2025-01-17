# Generated by Django 5.1.4 on 2024-12-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_lecturer_first_name_remove_lecturer_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturer',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]
