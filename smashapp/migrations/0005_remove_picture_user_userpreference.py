# Generated by Django 4.2.3 on 2023-09-23 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0004_delete_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="picture",
            name="user",
        ),
        migrations.CreateModel(
            name="UserPreference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=256)),
                ("liked", models.BooleanField()),
                (
                    "picture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="smashapp.picture",
                    ),
                ),
            ],
        ),
    ]