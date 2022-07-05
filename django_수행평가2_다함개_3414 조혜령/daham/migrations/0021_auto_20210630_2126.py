# Generated by Django 2.2.23 on 2021-06-30 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daham', '0020_auto_20210630_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='application',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='daham.Profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='daham.Profile'),
            preserve_default=False,
        ),
    ]
