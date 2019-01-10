# Generated by Django 2.1.5 on 2019-01-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellido', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=30)),
                ('DNI', models.IntegerField()),
                ('FechaNacimiento', models.DateField()),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1)),
            ],
        ),
    ]
