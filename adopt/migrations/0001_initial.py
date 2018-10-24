# Generated by Django 2.1.2 on 2018-10-24 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Perrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('H', 'Hembra'), ('M', 'Macho')], max_length=30)),
                ('fecha_ingreso', models.DateTimeField(blank=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='perrito',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt.Raza'),
        ),
    ]