# Generated by Django 2.1.7 on 2019-09-07 09:28

import common.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_buku_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('thumbnail', models.ImageField(blank=True, default=None, null=True, upload_to='article/thumbnail/%Y/%m/%D/')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='article/image/%Y/%m/%D/')),
                ('judul', models.CharField(default=None, max_length=255, null=True)),
                ('kata_kunci', models.CharField(default=None, max_length=255, null=True)),
                ('deskripsi_pendek', models.CharField(default=None, max_length=255, null=True)),
                ('isi_berita', common.fields.BinaryTextField()),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='article/image/%Y/%m/%D/'),
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='article/thumbnail/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='back',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bookImage/back/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='cover',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bookImage/cover/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='buku',
            name='thumbnail',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bookImage/thumbnail/%Y/%m/%D/'),
        ),
    ]
