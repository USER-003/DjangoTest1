# Generated by Django 4.2.7 on 2023-11-21 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('altura', models.FloatField()),
                ('medico_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FormApp.medico')),
            ],
        ),
    ]
