# Generated by Django 3.1.8 on 2021-06-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='likes',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
