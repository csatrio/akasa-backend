# Generated by Django 2.1.7 on 2019-09-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20190907_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliate',
            name='alamat_toko',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
