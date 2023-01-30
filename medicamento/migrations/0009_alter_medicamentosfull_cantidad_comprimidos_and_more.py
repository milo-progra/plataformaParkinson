# Generated by Django 4.1.4 on 2023-01-24 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0008_alter_medicamentosfull_medida_medicamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentosfull',
            name='cantidad_comprimidos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad Medicamento'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='forma_farmaceutica',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='forma formaceutica'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='recomendacion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='recomendacion de consumo'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='stockDiario',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stock diario'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='stockSistema',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='stock de sistema'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='tipo_farmaco',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='tipo de farmaco'),
        ),
        migrations.AlterField(
            model_name='medicamentosfull',
            name='via_ingesta',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='via de ingesta'),
        ),
    ]
