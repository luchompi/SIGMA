# Generated by Django 4.0.3 on 2022-04-05 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('NIT', models.CharField(error_messages={'unique': 'Ya está registrado esta identificacion'}, max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='NIT/RUT de proveedor')),
                ('razonSocial', models.CharField(max_length=100, verbose_name='Nombre/Razón Social de Proveedor')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección de la empresa')),
                ('dir_venta', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección de Punto de Venta (Si hubiere)')),
                ('telefono1', models.CharField(max_length=20, verbose_name='Telefono de Contacto')),
                ('telefono2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono de contacto Segundario (Si hubiere)')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electronico de contacto (Si hubiere)')),
                ('vendedor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre de contacto con la entidad/persona')),
                ('tel_vendedor', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono de vendedor')),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('identificacion', models.IntegerField(error_messages={'unique': 'Ya está registrado esta Identificación'}, primary_key=True, serialize=False, unique=True, verbose_name='Identificacion de Funcionario')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres del Funcionario')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos del Funcionario')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion de residencia')),
                ('telefono', models.CharField(max_length=100, verbose_name='Teléfono de Contacto')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo electronico')),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('sede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Empresa.sededependencia', verbose_name='Sede a la la que está adscrito')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
