# Generated by Django 2.2 on 2021-06-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_note', '0011_auto_20210601_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dt_created',
            field=models.DateField(auto_now_add=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='post',
            name='dt_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Modified'),
        ),
    ]
