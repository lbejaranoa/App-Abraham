from django.db import models
from apps.base.models import BaseModel
from apps.customers.models import Enterprice
from apps.parameters.models import Currency
from apps.services.models import Services

# Create your models here.
class SalesOrder(BaseModel):
    numero=models.CharField('Número orden', max_length = 255, blank = True, null = True)
    name=models.CharField('Nombre', max_length = 255, blank = True, null = True)
    idCurrency=models.ForeignKey(Currency,on_delete=models.CASCADE,verbose_name='Moneda',blank = True, null = True)
    amountTotal=models.DecimalField('Monto Total',decimal_places=2,max_digits=10, blank = True, null = True)
    amountHour=models.DecimalField('Monto',decimal_places=2,max_digits=10, blank = True, null = True)
    numberHours=models.IntegerField('Horas',blank = True, null = True)
    date=models.DateField('Fecha orden', max_length = 255, blank = True, null = True)
    idEnterprice=models.ForeignKey(Enterprice,on_delete=models.CASCADE,verbose_name='Empresa',blank = True, null = True)
    idService=models.ForeignKey(Services,on_delete=models.CASCADE,verbose_name='Servicio',blank = True, null = True)
    numberHoursSaldo=models.IntegerField('Saldo horas',blank = True, null = True)
    amountTotalUsed=models.DecimalField('Monto usado',decimal_places=2,max_digits=10, blank = True, null = True)
    class Meta: 
        verbose_name='Order de compra'
        verbose_name_plural='Ordenes de compra'
    
    def __str__(self):
        return self.name