from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
import random
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import (
    extend_schema,
    OpenApiExample,
    OpenApiResponse
)
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,'index.html')   


def health(request):
    return JsonResponse({
        "api": "SafeEdu API",
        "version": "1.0",
        "status": "online"
    })

from rest_framework import viewsets

from .models import (
    Escola,
    Comentario,
    Reacao,
    Motd,
    Imagem,
    LoginLog,
)

from .serializers import (
    EscolaSerializer,
    ComentarioSerializer,
    ReacaoSerializer,
    MotdSerializer,
    ImagemSerializer,
    LoginSerializer,
    LoginResponseSerializer,
    ValidateTokenResponseSerializer
)


@extend_schema(
    summary="Listar Escolas",
    description="""Retorna todas as escolas cadastradas.""",
    tags=["Escolas"]
)
class EscolaViewSet(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer

    http_method_names = ["get"]


@extend_schema(
    summary="Cadastrar Comentário",
    description="""Adiciona um comentário para uma escola.""",
    tags=["Comentários"])
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.select_related(
        "autor",
        "escola"
    )
    serializer_class = ComentarioSerializer

    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]    

    def get_queryset(self):
        queryset = super().get_queryset()

        id_escola = self.request.query_params.get("id_escola")

        if id_escola:
            queryset = queryset.filter(escola_id=id_escola)

        return queryset

    #para permitir filtrar por escolas GET /api/comentarios/?id_escola=3
    @action(detail=False, url_path=r"escola/(?P<id_escola>\d+)")

    def escola(self, request, id_escola=None):

        comentarios = (
            self.queryset
                .filter(escola_id=id_escola)
                .order_by("-data_hora")
        )

        serializer = self.get_serializer(
            comentarios,
            many=True
        )

        return Response(serializer.data)


@extend_schema(tags=["Reações"])
class ReacaoViewSet(viewsets.ModelViewSet):

    queryset = Reacao.objects.select_related(
        "autor",
        "comentario"
    )
    serializer_class = ReacaoSerializer

    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]



class MotdAPIView(GenericAPIView):
    serializer_class = MotdSerializer

    @extend_schema(
        tags=["MOTD"],
        summary="Mensagem motivacional",
        description="Retorna uma mensagem motivacional aleatória.",
        responses={200: MotdSerializer},
    )

    def get(self, request):

        mensagens = Motd.objects.all()

        if not mensagens.exists():
            return Response(
                {"detail": "Nenhuma mensagem cadastrada."},
                status=404
            )

        mensagem = random.choice(mensagens)

        serializer = MotdSerializer(mensagem)

        return Response(serializer.data)

# ACTION para implementar> GET /api/prints/usuario/aluno@escola.com/
@extend_schema(tags=["Prints"])
class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    queryset = Imagem.objects.select_related(
        "usuario"
    )
    serializer_class = ImagemSerializer

    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]    

    @action(
        detail=False,
        methods=["get"],
        url_path=r"usuario/(?P<email>.+)"
    )

    def por_usuario(self, request, email=None):

        prints = (
                self.queryset
                    .filter(usuario__email=email)
                    .order_by("-data_upload")
        )        

        serializer = self.get_serializer(
            prints,
            many=True
        )

        return Response(serializer.data)


class AuthAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    authentication_classes = []
    @extend_schema(
        tags=["Autenticação"],
        summary="Realizar Login",
        request=LoginSerializer,
        responses={200: LoginResponseSerializer},
        examples=[
            OpenApiExample(
                "Login",

                value={
                    "email": "admin@gmail.com",

                    "password": "123456"
                },

                request_only=True,
            )
        ],
        description="""
            Autentica um usuário e retorna um Access Token JWT.
            O campo **email** aceita tanto:

            - endereço de e-mail
            - nome de usuário (username)

            Exemplos:

            - gregmaster@gmail.com
            - gregmaster            

            ## Fluxo de autenticação

            1. Execute este endpoint.
            2. Copie o campo **access** retornado.
            3. Clique em **Authorize** no topo do Swagger.
            4. Cole: o token no formato Bearer <access_token>.
            5. Agora todos os endpoints protegidos poderão ser utilizados.
            """
    )
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        login = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        if "@" in login:
            try:
                usuario = User.objects.get(email=login)
                username = usuario.username
            except User.DoesNotExist:
                username = login
        else:
            username = login

        user = authenticate(
            username=username,
            password=password
        )


        if user is None:

            LoginLog.objects.create(
                usuario=None,
                ip_address=request.META.get("REMOTE_ADDR"),
                status="Falha"
            )

            return Response(
                {
                    "detail": "Usuário ou senha inválidos."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        LoginLog.objects.create(
            usuario=user,
            ip_address=request.META.get("REMOTE_ADDR"),
            status="Sucesso"
        )

        return Response({

            "access": str(refresh.access_token),

            "refresh": str(refresh),

            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }

        })


@extend_schema(
    tags=["Autenticação"],
    summary="Validar Token",
    description="Verifica se o JWT é válido.",
    responses={
        200: OpenApiResponse(description="Token válido"),
        401: OpenApiResponse(description="Token inválido"),
    }
)

class ValidateTokenAPIView(GenericAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = ValidateTokenResponseSerializer

    @extend_schema(
        tags=["Autenticação"],
        summary="Validar Token",
        responses={200: ValidateTokenResponseSerializer},
    )
    def get(self, request):

        return Response({
            "valid": True,
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email,
            }
        })