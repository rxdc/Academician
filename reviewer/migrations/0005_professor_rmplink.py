# Generated by Django 2.1.5 on 2019-03-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0004_auto_20190223_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='rmpLink',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
