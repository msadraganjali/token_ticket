from django.db import models

# Create your models here.
class Trakoneshs(models.Model):
    id1 = models.IntegerField()
    code = models.CharField(max_length= 20)
    trx_id = models.CharField(max_length= 20)
    cellphone = models.CharField(max_length= 20)