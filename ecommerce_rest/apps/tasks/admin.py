from django.contrib import admin
from apps.tasks.models import * 
# Register your models here.
from apps.customers.models import Customers,Enterprice
from apps.contracts.models import CustomerContractService
from apps.invoices.models import StatusInvoice


from django.core.validators import MaxValueValidator, MinValueValidator




class TasksServicesAdminSite(admin.ModelAdmin):
    model=TasksServices
    fields=['name','idContract','timeSpendHoras','timeSpendMinutos','idStatusTask','idUser']
    actions=['ProcesarFacturacion']
    list_display=('name','idContract','timeSpendHoras','timeSpendMinutos','idStatusTask','idUser','state')
    def ProcesarFacturacion(self,request,queryset):
        id=StatusInvoice.objects.filter(name="Procesada").first()
        print(id)
        print(id.id)
        queryset.update(idStatusInvoice=id.id)
        class Meta: 
            verbose_name='procesar facturación'
            verbose_name_plural='Procesar'


admin.site.register(StatusTask)

admin.site.register(TasksServices,TasksServicesAdminSite)