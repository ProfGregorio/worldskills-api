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
        related_name="comentarios",
        db_column="id_escola"
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )

    resposta = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="respostas"
    )


    comentario = models.TextField()

    data_hora = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_hora"]

    def __str__(self):
        return self.comentario[:40]        

class Reacao(models.Model):

    LIKE = "like"
    FAVORITO = "fav"

    TIPOS = [
        (LIKE, "Like"),
        (FAVORITO, "Favorito"),
    ]

    comentario = models.ForeignKey(
        Comentario,
        on_delete=models.CASCADE,
        related_name="reacoes",
        db_column="id_comentario"
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    tipo_reacao = models.CharField(
        max_length=10,
        choices=TIPOS
    )

    data_hora_reacao = models.DateTimeField(auto_now_add=True)



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

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    data_upload = models.DateTimeField(auto_now_add=True)

    imagem = models.ImageField(
        upload_to="prints/"
    )        
    class Meta:
        verbose_name = "Imagem (print) associada a um usuário"
        verbose_name_plural = "Imagem (print) associada a um usuário"

    def __str__(self):
        return f"Imagem {self.id}"        

class LoginLog(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    ip_address = models.GenericIPAddressField()

    status = models.CharField(max_length=20)

    data_hora = models.DateTimeField(auto_now_add=True)