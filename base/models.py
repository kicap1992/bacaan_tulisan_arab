from django.db import models

# Create your models here.
class tb_bacaan(models.Model):
    # id_bacaan = models.AutoField(primary_key=True)
    judul_bacaan = models.CharField(max_length=100)
    kategori = models.CharField(max_length=1)
    image_url = models.TextField(null=True, blank=True)
    audio_url = models.TextField(null=True, blank=True)
    list_per_page = 10
    def __str__(self):
        return self.judul_bacaan