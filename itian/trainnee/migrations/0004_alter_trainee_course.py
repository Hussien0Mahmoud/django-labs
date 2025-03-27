# Generated by Django 5.1.7 on 2025-03-27 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_id'),
        ('trainnee', '0003_alter_trainee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainees', to='course.course'),
        ),
    ]
