# Generated by Django 4.0.2 on 2022-02-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizzes',
            old_name='time_limits_mins',
            new_name='time_limit_mins',
        ),
    ]
