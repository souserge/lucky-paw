# Generated by Django 2.0.4 on 2018-04-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180416_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_housetrained',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_spayed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_specialcare',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_vaccinated',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]