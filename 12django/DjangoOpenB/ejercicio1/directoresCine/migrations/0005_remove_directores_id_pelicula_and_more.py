# Generated by Django 4.1.2 on 2022-11-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directoresCine', '0004_alter_directores_id_pelicula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='directores',
            name='id_pelicula',
        ),
        migrations.AddField(
            model_name='directores',
            name='Fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='directores',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre del Director'),
        ),
    ]
