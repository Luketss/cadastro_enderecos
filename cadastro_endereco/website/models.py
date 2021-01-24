from django.db import models

class Endereco(models.Model):

    cep = models.IntegerField(
        max_length=8,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    numero = models.IntegerField(
        max_length=10,
        null=False,
        blank=False
    )

    complemento = models.CharField(
        max_length=255,
        null=False,
        blank=True
    )

    bairro = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cidade = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    uf = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )

    descricao = models.CharField(
        max_length=255,
        null=False,
        blank=True
    )
