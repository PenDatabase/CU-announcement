# Generated by Django 5.1.4 on 2024-12-25 12:25

import django.core.validators
import django.db.models.deletion
import user.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_student_matric_no_student_reg_no'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='matric_no',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{2}+[a-zA-Z]{2}+[0-9]{6}$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
