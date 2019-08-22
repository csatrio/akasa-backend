from django.db import models
from common.models import BaseModel
from common.fields import BinaryTextField
from common.helpers import millis


# Create your models here.
# Add attribute is_automatic = False if you don't want to auto create admin and endpoint
class Kategori(BaseModel):
    class Meta:
        db_table = 'kategori'

    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori


class Buku(BaseModel):
    class Meta:
        db_table = 'buku'

    kategori = models.ForeignKey(Kategori, on_delete=models.DO_NOTHING, default=-1)
    nama = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)
    tanggal_terbit = models.DateField()
    review = BinaryTextField()
    cover = models.ImageField(upload_to=f"bookImage/cover/%Y/%m/%D/", default=None, null=True, blank=True)
    back = models.ImageField(upload_to=f"bookImage/back/%Y/%m/%D/", default=None, null=True, blank=True)
    thumbnail = models.ImageField(upload_to=f"bookImage/thumbnail/%Y/%m/%D/", default=None, null=True, blank=True)
    harga = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.nama


class Article(BaseModel):
    class Meta:
        db_table = 'article'

    judul = models.CharField(max_length=255, null=True, default=None)
    kata_kunci = models.CharField(max_length=255, null=True, default=None)
    deskripsi_pendek = models.CharField(max_length=255, null=True, default=None)
    isi_artikel = BinaryTextField()
