# Generated by Django 2.2.24 on 2021-06-30 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('begin_vegan', '0003_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]
