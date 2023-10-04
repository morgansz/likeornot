# Generated by Django 4.2.3 on 2023-09-26 13:44

from django.db import migrations

def add_initial_pictures(apps, schema_editor):
    Picture = apps.get_model('smashapp', 'Picture')
    picture = Picture(image='images/01.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/02.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/03.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/04.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/05.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/06.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/07.jpg')  # 确保此路径是正确的
    picture.save()
    # 这里你可以添加代码来创建和保存 Picture 对象
    # 例如：
    # picture = Picture(image='path/to/your/image.jpg')
    # picture.save()

class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0016_auto_20230926_1337"),
    ]

    operations = [
        migrations.RunPython(add_initial_pictures),
]
    