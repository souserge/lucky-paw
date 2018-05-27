# Generated by Django 2.0.4 on 2018-04-19 12:18

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20180418_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='pet_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_type',
            new_name='animaltype',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_breed',
            new_name='breed',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_gallery',
            new_name='gallery',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_housetrained',
            new_name='housetrained',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_size',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_spayed',
            new_name='spayed',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_specialcare',
            new_name='specialcare',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_supervisor',
            new_name='supervisor',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='pet_vaccinated',
            new_name='vaccinated',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='pet_photo',
        ),
        migrations.AddField(
            model_name='pet',
            name='photo',
            field=models.ImageField(default='', upload_to=app.models.pet_directory_path),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(default='', upload_to=app.models.pet_directory_path),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='super_photo',
            field=models.ImageField(default='', upload_to=app.models.user_directory_path),
        ),
    ]
