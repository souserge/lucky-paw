# Generated by Django 2.0.4 on 2018-04-19 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20180419_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisor',
            old_name='super_photo',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='supervisor',
            name='email',
        ),
    ]
