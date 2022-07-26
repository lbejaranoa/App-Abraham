# Generated by Django 3.1.7 on 2022-07-26 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20220724_1854'),
        ('orders', '0009_auto_20220725_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsalesorder',
            name='amountTotalUsed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monto usado'),
        ),
        migrations.AddField(
            model_name='historicalsalesorder',
            name='numberHoursSaldo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Saldo horas'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='amountTotalUsed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Monto usado'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='numberHoursSaldo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Saldo horas'),
        ),
        migrations.AlterField(
            model_name='historicalsalesorder',
            name='idService',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.services', verbose_name='Servicio'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='idService',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Servicio'),
        ),
    ]
