from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel
# Create your models here.
class Enterprice(BaseModel):
    name= models.CharField('Nombre', max_length = 255, blank = True, null = True)
    ruc =models.CharField('Ruc', max_length = 30, blank = True, null = True)
    class Meta: 
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    
    def __str__(self):
        return  f'{self.name}' 
        
class Customers(BaseModel):
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    phone = models.CharField('Teléfono', max_length = 255, blank = True, null = True)
    idEnterpriceCustomer=models.ForeignKey(Enterprice,on_delete=models.CASCADE, blank = True, null = True)
    
    class Meta: 
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
    
    def __str__(self):
        return f'Cliente: {self.name} {self.last_name}' 

