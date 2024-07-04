# Generated by Django 5.0.6 on 2024-06-15 05:09

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='displayed_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=16, unique=True)),
                ('display_name', models.CharField(max_length=125)),
                ('display_info', models.CharField(blank=True, default='', max_length=125)),
                ('display_color', colorfield.fields.ColorField(default='#575757', image_field=None, max_length=25, samples=None)),
                ('variable_price', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Displayed Item',
            },
        ),
    ]
