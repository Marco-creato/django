from django.db import models
from produto.models import Produto
from cliente.models import Cliente

# Create your models here.

class itemCarrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def total_preco(self):
        return self.quantidade * self.produto.preco

    def __str__(self):
        return f"{self.quantidade} de {self.produto.nome}"