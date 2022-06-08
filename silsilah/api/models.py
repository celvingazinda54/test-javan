from django.db import models

# Create your models here.

class keluarga(models.Model):
    nama = models.CharField(max_length=10)
    jenis_kelamin = models.CharField(max_length=1)
    status = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nama