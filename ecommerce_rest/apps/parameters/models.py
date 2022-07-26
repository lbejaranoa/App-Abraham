from django.db import models
from apps.base.models import BaseModel

# Create your models here.
class Currency(BaseModel):
    name=models.CharField('Moneda', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Moneda'
        verbose_name_plural='Monedas'
    
    def __str__(self):
        return self.name