from rest_framework import serializers

from .models import (
    Escola,
    Comentario,
    Motd,
    Imagem,
)


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


class MotdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motd
        fields = "__all__"


class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = "__all__"