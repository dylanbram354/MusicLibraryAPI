# Generated by Django 3.1.8 on 2021-06-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210611_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]