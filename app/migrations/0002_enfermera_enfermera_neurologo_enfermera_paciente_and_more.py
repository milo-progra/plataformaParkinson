# Generated by Django 4.1.4 on 2023-02-06 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_alter_usuario_tipo_usuario'),
        ('medicamento', '0012_rename_frecueniastock_medicamentosfull_frecuenciastock'),
        ('fonoaudiologo', '0006_alter_fonoaudiologo_email_fonoaudiologo_and_more'),
        ('medico_y_enfermera', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paciente', '0004_alter_familiar_email_familiar_and_more'),
        ('app', '0001_initial'),
    ]

    operations = [
        
    ]