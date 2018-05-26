# Generated by Django 2.0.4 on 2018-05-26 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20180521_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdopterInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone_number', models.CharField(default='', max_length=50)),
                ('adopted_pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pet')),
            ],
        ),
    ]
