# Generated by Django 4.2.3 on 2023-09-22 14:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0002_user_is_active_user_is_staff"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
    ]
