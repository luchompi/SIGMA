# Generated by Django 4.0.3 on 2022-04-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bajas', '0006_alter_detallebaja_fechaborrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallebaja',
            name='fechaBorrado',
            field=models.DateField(),
        ),
    ]
