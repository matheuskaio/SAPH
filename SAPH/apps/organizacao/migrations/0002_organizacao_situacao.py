# Generated by Django 2.2.1 on 2019-05-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacao',
            name='situacao',
            field=models.BooleanField(default=True),
        ),
    ]