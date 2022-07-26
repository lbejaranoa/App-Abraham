from django.db import models
from apps.base.models import BaseModel
from apps.services.models import Services,TypeSchedule
from apps.customers.models import Customers
from apps.orders.models import SalesOrder
# Create your models here.


class TypeContract(BaseModel):
    name=models.CharField('Nombre', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Tipo contrato'
        verbose_name_plural='Tipos contrato'
    
    def __str__(self):
        return self.name

class CustomerContractService(BaseModel):
    idService=models.ForeignKey(Services,on_delete=models.CASCADE, verbose_name='Servicio')
    idTypeContract=models.ForeignKey(TypeContract,on_delete=models.CASCADE,verbose_name='Tipo contrato',blank = True, null = True)
    idCustomer=models.ForeignKey(Customers,on_delete=models.CASCADE,verbose_name='Cliente')
    precio= models.DecimalField("Precio", decimal_places=2,max_digits=10, blank = True, null = True)
    idOrder= models.ForeignKey(SalesOrder, on_delete=models.CASCADE,verbose_name='Orden de compra',blank = True, null = True)
    dateBegin=models.DateField('Fecha Inicio contrato', max_length = 255, blank = True, null = True)
    dateEnd=models.DateField('Fecha Vencimiento contrato', max_length = 255, blank = True, null = True)
    dateComputation=models.DateField('Fecha Proceso contrato', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Contrato'
        verbose_name_plural='Contratos'
    def __str__(self):
        return f'Contrato {self.idCustomer} {self.idService}: {self.idTypeContract}' 
