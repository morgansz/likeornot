# Generated by Django 4.2.3 on 2023-09-22 14:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0003_remove_user_is_active_remove_user_is_staff"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
