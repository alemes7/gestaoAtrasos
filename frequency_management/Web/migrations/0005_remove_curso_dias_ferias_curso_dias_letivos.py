# Generated by Django 5.1.1 on 2024-10-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_curso_carga_horaria_intervalo_curso_dias_ferias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='dias_ferias',
        ),
        migrations.AddField(
            model_name='curso',
            name='dias_letivos',
            field=models.IntegerField(default='80'),
        ),
    ]