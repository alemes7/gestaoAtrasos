# Generated by Django 5.1.1 on 2024-10-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_curso_data_fim_curso_data_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='carga_horaria',
            field=models.IntegerField(default=1200),
        ),
    ]