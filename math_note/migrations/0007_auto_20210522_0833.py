# Generated by Django 2.2 on 2021-05-22 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_note', '0006_auto_20210522_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='example',
        ),
        migrations.AlterField(
            model_name='post',
            name='book',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='page',
            field=models.IntegerField(null=True),
        ),
    ]
