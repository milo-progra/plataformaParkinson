# Generated by Django 4.1.4 on 2022-12-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animo',
            fields=[
                ('id_Animo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Animo')),
                ('valor_animo', models.IntegerField(verbose_name='Valor Animo')),
                ('nombre_animo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Animo')),
            ],
        ),
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id_diabetes', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Diabetes')),
                ('tipo_diabetes', models.CharField(max_length=100, verbose_name='Tipo Diabetes')),
            ],
        ),
    ]
