# Generated by Django 2.2.1 on 2019-05-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=30)),
                ('itens', models.ManyToManyField(related_name='itens_solicitacao', to='item.Item')),
            ],
            options={
                'verbose_name_plural': 'Solicitações',
            },
        ),
    ]
