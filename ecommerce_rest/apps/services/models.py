from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
from apps.customers.models import Customers,Enterprice
from apps.users.models import User




from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class   Services(BaseModel):
    name = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    
    class Meta: 
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
    
    def __str__(self):
        return self.name


class TypeSchedule(BaseModel):
    name=models.CharField('Nombre', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Tipo facturación'
        verbose_name_plural='Tipo facturaciones'
    
    def __str__(self):
        return self.name


