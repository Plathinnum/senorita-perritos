# Generated by Django 2.1.2 on 2018-10-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_auto_20181023_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='perrito',
            name='descripcion',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
