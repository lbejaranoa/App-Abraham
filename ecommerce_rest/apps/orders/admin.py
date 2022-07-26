from django.contrib import admin
from apps.orders.models import * 
# Register your models here.

class OrdersAdminSite(admin.ModelAdmin):
    model=SalesOrder
    fields=[]
    #actions=['ProcesarFacturacion']
    list_display=(
        'name'
        ,'idEnterprice'
        ,'idService'
        ,'numberHoursSaldo'
        ,'amountTotalUsed'
        )
    
    
    '''def ProcesarFacturacion(self,request,queryset):
        print("asd")
       
        id=StatusInvoice.objects.filter(name="Procesada").first()
        print(id.id)
        queryset.update(idStatusInvoice=id.id)
       
        class Meta: 
            verbose_name='procesar facturación'
            verbose_name_plural='Procesar'
            '''


admin.site.register(SalesOrder,OrdersAdminSite)