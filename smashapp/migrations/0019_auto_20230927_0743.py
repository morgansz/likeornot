# Generated by Django 4.2.3 on 2023-09-27 07:43

from django.db import migrations

def add_initial_pictures(apps, schema_editor):
    Picture = apps.get_model('smashapp', 'Picture')
    picture = Picture(image='images/08.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/09.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/10.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/11.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/12.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/13.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/14.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/15.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/16.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/17.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/18.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/19.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/20.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/21.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/22.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/23.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/24.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/25.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/26.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/27.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/28.jpg')  # 确保此路径是正确的
    picture.save()

    picture = Picture(image='images/29.jpg')  # 确保此路径是正确的
    picture.save()


    # 这里你可以添加代码来创建和保存 Picture 对象
    # 例如：
    # picture = Picture(image='path/to/your/image.jpg')
    # picture.save()

class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0018_auto_20230926_1353"),
    ]

    operations = [
        migrations.RunPython(add_initial_pictures),
    ]
