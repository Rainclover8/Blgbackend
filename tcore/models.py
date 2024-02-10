from django.db import models

# Create your models here.
class YazilarModels(models.Model):
    yaziFotosu = models.FileField(upload_to="resimler/")
    yaziAdi = models.CharField(max_length=50)
    yaziAltBaslik = models.CharField(max_length=30)
    yaziAciklama = models.TextField(verbose_name="aciklama")
    
    def __str__(self):
        return self.yaziAdi