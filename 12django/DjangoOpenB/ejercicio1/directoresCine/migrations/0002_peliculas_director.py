# Generated by Django 4.1.2 on 2022-10-27 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directoresCine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peliculas',
            name='director',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='directoresCine.directores'),
            preserve_default=False,
        ),
    ]