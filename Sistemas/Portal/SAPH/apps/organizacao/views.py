from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView

from apps.funcionario.models import Funcionario
from .models import Organizacao


class CadastrarOrganizacao(CreateView):
    model = Organizacao
    fields = ['nome', 'cnpj', 'endereco', 'telefone']

    def form_valid(self, form):
        organizacao = form.save(commit=False)
        organizacao.save()
        # identificador = organizacao.pk
        # funcionario = Funcionario.objects.filter(pk=self.request.user.funcionario.pk)
        funcionario = get_object_or_404(Funcionario, pk=self.request.user.funcionario.pk)
        funcionario.organizacao = organizacao

        funcionario.save()

        return super(CadastrarOrganizacao, self).form_valid(form)


class AtualizarOrganizacao(UpdateView):
    model = Organizacao
    fields = ['nome', 'cnpj', 'endereco', 'telefone']

    def get_queryset(self):
        return Organizacao.objects.filter(pk=self.kwargs['pk'])

    template_name_suffix = '_update_form'

class ListarOrganizacao(ListView):
    model = Organizacao

    def get_queryset(self):
        return Organizacao.objects.all()
