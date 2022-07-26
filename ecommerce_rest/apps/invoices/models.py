from django.db import models
from apps.base.models import BaseModel
from apps.orders.models import SalesOrder
from apps.contracts.models import CustomerContractService
from apps.customers.models import Enterprice
from apps.tasks.models import TasksServices



class StatusInvoice(BaseModel):
    name=models.CharField('Nombre', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Estado facturación'
        verbose_name_plural='Estados facturacion'
    
    def __str__(self):
        return self.name

# Create your models here.
class InvoiceDocument(BaseModel):
    idSalesOrder= models.ForeignKey(SalesOrder,on_delete=models.CASCADE, blank = True, null = True)
    dateRegister=models.DateField('Fecha registro', max_length = 255, blank = True, null = True)
    dateTranference=models.DateField('Fecha deposito', max_length = 255, blank = True, null = True)
    amount=models.DecimalField('Monto',decimal_places=10,max_digits=10, blank = True, null = True)
    idEnterpriceCustomer=models.ForeignKey(Enterprice,on_delete=models.CASCADE, blank = True, null = True)
    class Meta: 
        verbose_name='Factura'
        verbose_name_plural='Facturas'
    
    def __str__(self):
        return  f'Horas({self.dateRegister}:{self.dateTranference}) ' 


class InvoicesContracts(BaseModel):
    name= models.CharField('Nombre', max_length = 255, blank = True, null = True)
    idContract=models.ForeignKey(CustomerContractService,on_delete=models.CASCADE)
    idTask=models.ForeignKey(TasksServices,on_delete=models.CASCADE, blank = True, null = True)
    dateBegin=models.DateField('Fecha Inicio contrato', max_length = 255, blank = True, null = True)
    dateEnd=models.DateField('Fecha Vencimi contrato', max_length = 255, blank = True, null = True)
    idStatusInvoice=models.ForeignKey(StatusInvoice,on_delete=models.CASCADE,null=True)
    idInvoiceDocument=models.ForeignKey(InvoiceDocument,on_delete=models.CASCADE,null=True)
    class Meta: 
        verbose_name='Facturación contratos'
        verbose_name_plural='Facturaciones contratos'
    
    def __str__(self):
        return  f'Horas({self.timeSpendHoras}:{self.timeSpendMinutos}) Tarea:{self.name} {self.idContract}' 
