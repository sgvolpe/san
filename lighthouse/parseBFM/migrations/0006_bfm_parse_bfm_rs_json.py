# Generated by Django 2.1.1 on 2019-02-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parseBFM', '0005_auto_20190219_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='bfm_parse',
            name='bfm_rs_json',
            field=models.TextField(blank=True, null=True),
        ),
    ]
