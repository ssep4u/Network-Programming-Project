# Generated by Django 2.2.23 on 2021-06-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daham', '0014_auto_20210629_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
