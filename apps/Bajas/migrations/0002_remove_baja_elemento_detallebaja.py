# Generated by Django 4.0.3 on 2022-04-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_alter_elemento_estado_alter_elemento_tipoingreso'),
        ('Bajas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baja',
            name='elemento',
        ),
        migrations.CreateModel(
            name='DetalleBaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamps', models.DateTimeField(auto_now=True)),
                ('baja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bajas.baja')),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.elemento')),
            ],
        ),
    ]
