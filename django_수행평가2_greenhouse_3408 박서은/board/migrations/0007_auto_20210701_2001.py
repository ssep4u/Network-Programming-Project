# Generated by Django 2.2.24 on 2021-07-01 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20210701_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='introduction',
            new_name='text',
        ),
    ]
