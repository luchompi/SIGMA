# Generated by Django 4.0.3 on 2022-04-05 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(error_messages={'unique': 'Esta Marca ya se encuentra Registrada'}, max_length=50, unique=True)),
                ('timestamps', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(error_messages={'unique': 'Ya está registrado este modelo'}, max_length=150, unique=True)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('marca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('placa', models.AutoField(primary_key=True, serialize=False)),
                ('Serial', models.CharField(error_messages={'unique': 'Ya existe un elemento con este Serial'}, max_length=100, unique=True, verbose_name='Serial del Elemento')),
                ('conexionRed', models.BooleanField(default=False, verbose_name='Está conectado a la red?')),
                ('ip', models.GenericIPAddressField(blank=True, error_messages={'unique': 'Esta IP ya se encuentra en uso'}, null=True, unique=True, verbose_name='Dirección IP')),
                ('nombreRed', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre en la red')),
                ('mac', models.CharField(blank=True, error_messages={'unique': 'Ya existe un elemento con este MAC'}, max_length=100, null=True, unique=True, verbose_name='Dirección MAC')),
                ('valorAdquisicion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor de adquisición')),
                ('fechaAdquisicion', models.DateField(auto_now=True, verbose_name='Fecha de adquisición')),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Por Asignar', 'Pendiente'), ('En mantenimiento', 'Mantenimiento'), ('En Proceso de Baja', 'Baja')], default='Por Asignar', max_length=50)),
                ('tipoIngreso', models.CharField(choices=[('Donacion', 'Donacion'), ('Compra directa', 'Compra'), ('Comodato', 'Comodato'), ('Transferencia tecnológica', 'Transferencia'), ('Traspaso de otra Sede', 'Traspaso')], default='Compra directa', max_length=150)),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.modelo', verbose_name='Referencia del elemento')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Personas.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Elemento',
                'verbose_name_plural': 'Elementos',
            },
        ),
    ]
