# Generated by Django 2.1.7 on 2019-08-04 10:45

import common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190730_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('judul', models.CharField(default=None, max_length=255, null=True)),
                ('kata_kunci', models.CharField(default=None, max_length=255, null=True)),
                ('deskripsi_pendek', models.CharField(default=None, max_length=255, null=True)),
                ('isi_artikel', common.fields.BinaryTextField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.AddField(
            model_name='buku',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buku',
            name='back',
            field=models.ImageField(default=None, null=True, upload_to='bookImage/back/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='cover',
            field=models.ImageField(default=None, null=True, upload_to='bookImage/cover/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='thumbnail',
            field=models.ImageField(default=None, null=True, upload_to='bookImage/thumbnail/%Y/%m/%D/'),
        ),
    ]