# Generated by Django 2.2.23 on 2021-06-29 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daham', '0013_auto_20210629_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='photo',
            new_name='images',
        ),
    ]
