from measure.validate_positive import validate_positive
from django.db import models
import uuid


class Temphum(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    type = models.CharField(verbose_name='Tipo', max_length=20, null=True, blank=True)
#    value = models.IntegerField(verbose_name='Valor', null=True, blank=True)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
    codigo = models.CharField(verbose_name='codigo', max_length=10)
    latitud = models.CharField(verbose_name='latitud', max_length=10)
    longitud = models.CharField(verbose_name='longitud', max_length=10)
    producto = models.CharField(verbose_name='producto', max_length=30)
    area = models.IntegerField(verbose_name='area', validators=[validate_positive], null=True, blank=True)


    
