# Generated by Django 2.2.23 on 2021-06-30 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daham', '0018_auto_20210629_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
