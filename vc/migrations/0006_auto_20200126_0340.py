# Generated by Django 3.0.2 on 2020-01-25 23:40

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vc', '0005_auto_20200126_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=300, populate_from='title', unique=True),
        ),
    ]
