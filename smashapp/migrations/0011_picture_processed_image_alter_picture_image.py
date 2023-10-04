# Generated by Django 4.2.3 on 2023-09-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0010_alter_picture_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="picture",
            name="processed_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="processed_images/"
            ),
        ),
        migrations.AlterField(
            model_name="picture",
            name="image",
            field=models.ImageField(upload_to="original_images/"),
        ),
    ]
