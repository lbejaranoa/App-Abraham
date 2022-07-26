from django.contrib import admin
from apps.contracts.models import * 
# Register your models here.


class CustomerContractServiceAdminSite(admin.ModelAdmin):
    model=CustomerContractService
    fields=[
        'idService'
        ,'idTypeContract'
        ,'idCustomer'
        ,'idOrder'
        ,'dateBegin'
        ,'dateEnd'
        ,'dateComputation'
        ]
    actions=['ProcesarFacturacion']
    list_display=(
        'idService'
        ,'idTypeContract'
        ,'idCustomer'
        ,'idOrder'
        ,'dateBegin'
        ,'dateEnd'
        ,'dateComputation')
    
    
    def ProcesarFacturacion(self,request,queryset):
        print("asd")
        '''
        id=StatusInvoice.objects.filter(name="Procesada").first()
        print(id.id)
        queryset.update(idStatusInvoice=id.id)
        '''
        class Meta: 
            verbose_name='procesar facturación'
            verbose_name_plural='Procesar'

admin.site.register(CustomerContractService,CustomerContractServiceAdminSite)
admin.site.register(TypeContract)