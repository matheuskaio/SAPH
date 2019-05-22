# Generated by Django 2.2.1 on 2019-05-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('nivel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('funcionario', models.ManyToManyField(blank=True, to='funcionario.Funcionario')),
                ('gerente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gerentesetor', to='funcionario.Funcionario')),
                ('nivel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nivel.Nivel')),
            ],
            options={
                'verbose_name_plural': 'Setores',
            },
        ),
    ]
