# Generated by Django 5.0.1 on 2024-01-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudtransporte',
            name='id',
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='codigo_seguimiento',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
