# Generated by Django 5.0.6 on 2024-05-12 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='estado',
            field=models.CharField(choices=[('NOVA', 'Nova'), ('EM_ANDAMENTO', 'Em Andamento'), ('CONCLUIDA', 'Concluida'), ('CANCELADA', 'Cancelada')], default='NOVA', max_length=13),
        ),
    ]
