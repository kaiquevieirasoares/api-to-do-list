# Generated by Django 5.0.6 on 2024-05-12 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_api', '0002_tarefa_estado'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefa',
            new_name='Task',
        ),
    ]
