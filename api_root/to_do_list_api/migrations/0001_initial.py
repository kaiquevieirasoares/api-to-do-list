# Generated by Django 5.0.6 on 2024-05-12 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(default='', max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=250)),
                ('prazo', models.DateField()),
                ('conclusao', models.DateField()),
            ],
        ),
    ]
