# Generated by Django 2.2.24 on 2021-06-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begin_vegan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('전체', '전체'), ('비건', '비건'), ('락토-오보', '락토-오보'), ('페스코', '페스코'), ('폴로', '폴로'), ('플렉시테리언', '플렉시테리언')], default='플렉시테리언', max_length=6),
        ),
    ]
