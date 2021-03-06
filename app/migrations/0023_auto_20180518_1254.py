# Generated by Django 2.0.4 on 2018-05-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20180428_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adopted',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='housetrained',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='spayed',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='specialcare',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='vaccinated',
            field=models.NullBooleanField(),
        ),
    ]
