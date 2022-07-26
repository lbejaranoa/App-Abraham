from django.db import models
from simple_history.models import HistoricalRecords
from apps.contracts.models import CustomerContractService
from apps.base.models import BaseModel
from apps.users.models import User



from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class StatusTask(BaseModel):
    name=models.CharField('Nombre', max_length = 255, blank = True, null = True)
    class Meta: 
        verbose_name='Estado tarea'
        verbose_name_plural='Estado tareas'
    def __str__(self):
        return self.name

class TasksServices(BaseModel):
    name= models.CharField('Nombre', max_length = 255, blank = True, null = True)
    idContract=models.ForeignKey(CustomerContractService,on_delete=models.CASCADE)
    timeSpendHoras = models.IntegerField('Horas gastadas',validators=[
            MaxValueValidator(1000),
            MinValueValidator(0)
        ])
    timeSpendMinutos = models.IntegerField('Minutos gastados', validators=[
            MaxValueValidator(1000),
            MinValueValidator(0)
        ])
    idStatusTask=models.ForeignKey(StatusTask,on_delete=models.CASCADE,null=True)
    idUser=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta: 
        verbose_name='Tarea'
        verbose_name_plural='Tareas'
    
    def __str__(self):
        return  f'Horas({self.timeSpendHoras}:{self.timeSpendMinutos}) Tarea:{self.name} {self.idContract}' 
