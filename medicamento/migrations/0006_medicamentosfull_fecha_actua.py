# Generated by Django 4.1.4 on 2023-01-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamento', '0005_alter_medicamentosfull_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamentosfull',
            name='fecha_actua',
            field=models.DateTimeField(blank=True, null=True, verbose_name='fecha actualizacion stock'),
        ),
    ]