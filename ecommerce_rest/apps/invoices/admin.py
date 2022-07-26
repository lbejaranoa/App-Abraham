from django.contrib import admin
from apps.invoices.models import * 
# Register your models here.
class StatusInvoiceAdminSite(admin.ModelAdmin):
    model=StatusInvoice
    fields=['name','state']
    actions=['changeStatus']
    list_display=('name','state')
    def changeStatus(self,request,queryset):
        queryset.update(state=False)
