# Generated by Django 4.0.3 on 2022-04-18 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bajas', '0003_detallebaja_autorizado'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallebaja',
            name='fechaBorrado',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 14, 26, 50, 276816)),
        ),
    ]
