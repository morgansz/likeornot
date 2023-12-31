# Generated by Django 4.2.3 on 2023-09-26 13:32

from django.db import migrations

def remove_picture(apps, schema_editor):
    Picture = apps.get_model('smashapp', 'Picture')
    # 删除与 '01.jpg' 匹配的记录
    Picture.objects.filter(image='01.jpg').delete()
    Picture.objects.filter(image='02.jpg').delete()
    Picture.objects.filter(image='03.jpg').delete()
    Picture.objects.filter(image='1.jpg').delete()
    Picture.objects.filter(image='2.jpg').delete()
    Picture.objects.filter(image='3.jpg').delete()
    Picture.objects.filter(image='4.jpg').delete()








class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0014_auto_20230926_1218"),
    ]

    operations = [
        migrations.RunPython(remove_picture),
    ]
