# Generated by Django 2.2.1 on 2019-05-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='funcionarios_fotos'),
        ),
    ]