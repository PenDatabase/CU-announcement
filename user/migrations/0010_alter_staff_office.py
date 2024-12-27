# Generated by Django 5.1.4 on 2024-12-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_student_matric_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='office',
            field=models.CharField(choices=[('DSA', 'Dean of Student Affairs'), ('VC', 'Vice Chancellor'), ('DEPUTY VC', 'Deputy Vice Chancellor'), ('REGISTRAR', 'Registrar')], max_length=255, unique=True),
        ),
    ]