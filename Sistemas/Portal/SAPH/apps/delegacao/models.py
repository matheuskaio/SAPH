from django.db import models

# Create your models here.
from django.urls import reverse

from apps.item.models import Item


class Delegacao(models.Model):
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    itens = models.ManyToManyField(Item)
    status = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('cadasrtrar_delegacao')

    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name_plural = 'Solicitações'