# Generated by Django 2.1.5 on 2019-05-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0015_uloopreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professor',
            old_name='hitCounter',
            new_name='hit_counter',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='lastUpdated',
            new_name='last_updated',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='ratingPages',
            new_name='rating_pages',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='rmpLink',
            new_name='rmp_link',
        ),
        migrations.AddField(
            model_name='professor',
            name='uloop_link',
            field=models.CharField(default='None', max_length=50),
            preserve_default=False,
        ),
    ]
