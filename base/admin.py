from django.contrib import admin

# Register your models here.

from .models import tb_bacaan

class Filter_Bacaan(admin.ModelAdmin):
  list_display = ('judul_bacaan', 'kategori', 'image_url', 'audio_url')
  list_per_page = 10

admin.site.register(tb_bacaan, Filter_Bacaan)
