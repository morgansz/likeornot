# Generated by Django 4.2.3 on 2023-09-26 13:53

from django.db import migrations

def remove_picture(apps, schema_editor):
    Picture = apps.get_model('smashapp', 'Picture')
    # 删除与 '01.jpg' 匹配的记录
    Picture.objects.filter(image='images/02.jpg').delete()
    Picture.objects.filter(image='images/06.jpg').delete()
    
class Migration(migrations.Migration):
    dependencies = [
        ("smashapp", "0017_auto_20230926_1344"),
    ]

    operations = [
        migrations.RunPython(remove_picture),

    ]