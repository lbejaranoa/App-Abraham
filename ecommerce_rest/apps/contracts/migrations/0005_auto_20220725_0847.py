# Generated by Django 3.1.7 on 2022-07-25 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_auto_20220724_1854'),
        ('contracts', '0004_auto_20220725_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customercontractservice',
            name='idService',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services', verbose_name='Servicio1'),
        ),
        migrations.AlterField(
            model_name='historicalcustomercontractservice',
            name='idService',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='services.services', verbose_name='Servicio1'),
        ),
    ]
