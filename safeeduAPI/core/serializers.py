from rest_framework import serializers

from .models import (
    Escola,
    Comentario,
    Reacao,
    Motd,
    Imagem,
)


class EscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escola
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):

    autor_nome = serializers.CharField(
        source="autor.get_full_name",
        read_only=True
    )

    class Meta:
        model = Comentario
        fields = "__all__"


class ReacaoSerializer(serializers.ModelSerializer):

    nome_autor = serializers.CharField(
        source="autor.get_full_name",
        read_only=True
    )

    class Meta:
        model = Reacao
        fields = "__all__"


class ImagemSerializer(serializers.ModelSerializer):

    email_user = serializers.EmailField(
        source="usuario.email",
        read_only=True
    )

    class Meta:
        model = Imagem
        fields = "__all__"


class MotdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motd
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    #username = serializers.CharField()
    email = serializers.CharField(
        help_text="Informe o e-mail ou o nome de usuário."
    )
    password = serializers.CharField(write_only=True)

class UserInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()

class LoginResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()
    user = UserInfoSerializer()
    
class ValidateTokenResponseSerializer(serializers.Serializer):
    valid = serializers.BooleanField()
    user = UserInfoSerializer()

    