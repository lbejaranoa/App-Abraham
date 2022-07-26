# Generated by Django 3.1.7 on 2022-07-23 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_auto_20220723_1025'),
        ('services', '0006_auto_20220718_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDocument',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('dateRegister', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha registro')),
                ('dateTranference', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha deposito')),
                ('amount', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True, verbose_name='Monto')),
                ('idEnterpriceCustomer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.enterprice')),
                ('idSalesOrder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.salesorder')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.AddField(
            model_name='customercontractservice',
            name='dateBegin',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.AddField(
            model_name='customercontractservice',
            name='dateComputation',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.AddField(
            model_name='customercontractservice',
            name='dateEnd',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.AddField(
            model_name='historicalcustomercontractservice',
            name='dateBegin',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.AddField(
            model_name='historicalcustomercontractservice',
            name='dateComputation',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.AddField(
            model_name='historicalcustomercontractservice',
            name='dateEnd',
            field=models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato'),
        ),
        migrations.CreateModel(
            name='InvoicesContracts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('dateBegin', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato')),
                ('dateEnd', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Vencimi contrato')),
                ('idContract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.customercontractservice')),
                ('idInvoiceDocument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.invoicedocument')),
                ('idStatusInvoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.statusinvoice')),
                ('idTask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.tasksservices')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalInvoicesContracts',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('dateBegin', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Inicio contrato')),
                ('dateEnd', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha Vencimi contrato')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idContract', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.customercontractservice')),
                ('idInvoiceDocument', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.invoicedocument')),
                ('idStatusInvoice', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.statusinvoice')),
                ('idTask', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.tasksservices')),
            ],
            options={
                'verbose_name': 'historical Tarea',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInvoiceDocument',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('dateRegister', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha registro')),
                ('dateTranference', models.DateField(blank=True, max_length=255, null=True, verbose_name='Fecha deposito')),
                ('amount', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True, verbose_name='Monto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idEnterpriceCustomer', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customers.enterprice')),
                ('idSalesOrder', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.salesorder')),
            ],
            options={
                'verbose_name': 'historical Factura',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
