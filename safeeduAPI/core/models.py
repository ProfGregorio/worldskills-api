from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Escola(models.Model):
    nome = models.CharField(max_length=200)
    #endereco = models.CharField(max_length=255)
    #cidade = models.CharField(max_length=100)
    #estado = models.CharField(max_length=2)
    #telefone = models.CharField(max_length=20, blank=True)
    #email = models.EmailField(blank=True)
    #avaliacao = models.IntegerField()
    avaliacao = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10)]
    )
    image = models.ImageField(upload_to="uploads/") #models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()    
    #ativa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome
 

class Comentario(models.Model):
    # usuario = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     related_name="comentarios"
    # )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        db_column="id_escola",
        related_name="comentarios",
    )

    comentario = models.TextField()

    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_hora"]

    def __str__(self):
        return self.comentario[:40]        



class Motd(models.Model):
    motd = models.CharField(
        max_length=255,
        primary_key=True,
        db_column="MOTD"
    )


    class Meta:
        verbose_name = "Mensagem do Dia"
        verbose_name_plural = "Mensagens do Dia"

    def __str__(self):
        return self.motd

class Imagem(models.Model):
    # usuario = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE
    # )
    data_upload = models.DateTimeField(auto_now_add=True)

    #imagem = models.ImageField(upload_to="uploads/")
    imagem = models.BinaryField()

    # descricao = models.CharField(
    #     max_length=255,
    #     blank=True
    # )

    
    def __str__(self):
        return f"Imagem {self.id}"        