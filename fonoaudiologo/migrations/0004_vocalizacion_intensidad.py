# Generated by Django 4.1.4 on 2022-12-21 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_initial'),
        ('fonoaudiologo', '0003_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocalizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Monitoreo')),
                ('url_archivo_vocalizacion', models.FileField(upload_to='vocalizacion/')),
                ('duracion', models.IntegerField(null=True, verbose_name='Duracion')),
                ('bpminute', models.IntegerField(null=True, verbose_name='BPM Beats Per Minute ')),
                ('bpmeasure', models.IntegerField(null=True, verbose_name='Beats Per Measure')),
                ('comentario', models.CharField(max_length=500, null=True, verbose_name='Comentarios')),
                ('username_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Intensidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Monitoreo')),
                ('url_archivo_intensidad', models.FileField(upload_to='intensidad/')),
                ('intensidad', models.IntegerField(null=True, verbose_name='Intensidad')),
                ('mindb', models.IntegerField(null=True, verbose_name='Min dB')),
                ('maxdb', models.IntegerField(null=True, verbose_name='Max dB')),
                ('comentario', models.CharField(max_length=500, null=True, verbose_name='Comentarios')),
                ('username_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
