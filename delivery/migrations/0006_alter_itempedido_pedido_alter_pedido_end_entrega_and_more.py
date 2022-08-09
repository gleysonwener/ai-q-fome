# Generated by Django 4.1 on 2022-08-09 18:02

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('delivery', '0005_pedido_cod_pedido_end_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.pedido', verbose_name='Pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='end_entrega',
            field=address.models.AddressField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address', verbose_name='Endereço de entrega'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Aberto', 'Aberto'), ('Recebido', 'Recebido'), ('Em preparo', 'Em preparo'), ('Saiu para entrega', 'Saiu para entrega')], max_length=25, verbose_name='Status'),
        ),
    ]