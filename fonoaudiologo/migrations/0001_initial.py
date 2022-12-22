# Generated by Django 4.1.4 on 2022-12-21 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0002_alter_usuario_tipo_usuario'),
    
        ('medico_y_enfermera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonoaudiologo',
            fields=[
                ('id_fonoaudiologo', models.IntegerField(verbose_name='Id Usuario')),
                ('username_fonoaudiologo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rut_fonoaudiologo', models.CharField(max_length=10, verbose_name='Rut fonoaudiologo')),
                ('nombre_fonoaudiologo', models.CharField(max_length=100, verbose_name='Nombre fonoaudiologo')),
                ('apellido_fonoaudiologo', models.CharField(max_length=100, verbose_name='Apellido fonoaudiologo')),
                ('direccion_fonoaudiologo', models.CharField(max_length=100, verbose_name='Direccion fonoaudiologo')),
                ('email_fonoaudiologo', models.CharField(max_length=100, verbose_name='Email fonoaudiologo')),
                ('telefono_fonoaudiologo', models.CharField(blank=True, max_length=9, null=True, verbose_name='Telefono fonoaudiologo')),
                ('whatsaap_fonoaudiologo', models.CharField(max_length=9, verbose_name='Whatsaap fonoaudiologo')),
                ('celular_fonoaudiologo', models.CharField(max_length=9, verbose_name='Celular fonoaudiologo')),
                ('telegram_fonoaudiologo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telegram fonoaudiologo')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comuna', verbose_name='Comuna')),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='medico_y_enfermera.institucion', verbose_name='Institucion')),
            ],
        ),
    ]